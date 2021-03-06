#!/usr/bin/python

# sshlist v0.1
# Instructions

# 1. Copy file sshlist.py (this file) to /usr/local/bin
# 2. Edit file .sshlist in home directory to add ssh host (one per line)
# 3. You can if you wish add additional ssh options. The line is appended to the ssh command
# 4. Launch sshlist.py
# 5. Or better yet, add it to gnome startup programs list so it's run on login.

# v0.1 - Initial push
# v0.11 - Add a little polish.
# v0.12 - Modifications henceforth are made by Ben L blutgens@gmail.com
#       - Fix crash caused by not initializing pynotify
#       - Give ability to spawn more than one ssh process at a time 
# v0.13 -  Add Quit menu item.

import gobject
import gtk
import appindicator
import os
import sys
import pynotify

ver = "0.11"

def run_program(cmd):
    #returns (output, exit value)
    fd=os.popen(cmd,"r")
    output=fd.read()
    exitvalue=fd.close()
    return (output,exitvalue)

def menuitem_response(w, buf):
    if buf == "_about" :
        md = gtk.MessageDialog(None,0, gtk.MESSAGE_INFO,
             gtk.BUTTONS_OK)
        md.set_markup("<b>sshlist v%s</b>" % ver)
        md.format_secondary_markup("""A simple sshmenu like replacement for appindicator menu.

To add items to menu, simply edit the file <i>.sshlist</i> in your home directory (one host per line).

Author: anil.verve@gmail.com
http://www.gulecha.org""")
        md.run()
        md.destroy()
    elif buf == "_refresh":
        newmenu = build_menu()
        ind.set_menu(newmenu)
        # Initialize pynotify, without this it crashes on "Refresh"
        pynotify.init("SSHList Notification")
        pynotify.Notification("sshlist refreshed","Menu list was refreshed from ~/.sshlist").show()
    elif buf == "_quit":
        newmenu = build_menu()
        ind.set_menu(newmenu)
        gtk.mainquit()
    else:
        print "gnome-terminal -x ssh " + buf + " &"
        run_program("gnome-terminal -x ssh " + buf + " &")


def build_menu():
    # create a menu

    menu = gtk.Menu()

    # read in the ssh hosts list from ~/.sshlist
    hosts = open(os.getenv("HOME")+"/.sshlist","r").read()
    hostlist = hosts.split("\n")

    while "" in hostlist:
        hostlist.remove("")

    # create some
    for host in hostlist:
        menu_items = gtk.MenuItem(host)
        menu.append(menu_items)

        # this is where you would connect your menu item up with a function:
        menu_items.connect("activate", menuitem_response, host)
        # show the items
        menu_items.show()

    separator = gtk.SeparatorMenuItem()
    separator.show()
    menu.append(separator)

    menu_items = gtk.MenuItem("Refresh")
    menu.append(menu_items)
    menu_items.connect("activate", menuitem_response, "_refresh")
    menu_items.show()

    menu_items = gtk.MenuItem("About")
    menu.append(menu_items)
    menu_items.connect("activate", menuitem_response, "_about")
    menu_items.show()

    menu_items = gtk.MenuItem("Quit")
    menu.append(menu_items)
    menu_items.connect("activate", menuitem_response, "_quit")
    menu_items.show()
    return menu


if __name__ == "__main__":
    ind = appindicator.Indicator ("sshlist",
                                "gnome-netstatus-tx",
                                appindicator.CATEGORY_APPLICATION_STATUS)
    ind.set_label("SSH")
    ind.set_status (appindicator.STATUS_ACTIVE)
    ind.set_attention_icon ("connect_creating")
    try:
        with open(os.getenv("HOME")+"/.sshlist","r"):
            sshmenu = build_menu()
            ind.set_menu(sshmenu)
            gtk.main()
    except IOError:
        print os.getenv("HOME")+"/.sshlist doesn't exist. Please create it with one hostname per line and run",sys.argv[0],"again"

