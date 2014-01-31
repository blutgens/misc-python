Various files in this repo.

1. phoneresizer

Description: A script to resize all images in a folder for your phone/digital frame screen.

Requirements: Requires imagemagick to be installed on the system (apt-get install imagemagick). Place the file phoneresizer under /usr/local/bin (or someother entry in $PATH)

Usage: cd into the folder, and run 

  phoneresizer <longerside> <shortersize> [-cbz]

  phoneresizer 480 320

480/320 represent the longer shorter side on the screen. Two directories will be created: portrait and landscape. Images would be moved in there depending on their resolution, and they will be resized to the specified size.

  phoneresizer 480 320 -cbz

This will create cbz files from the two generated directories (and delete the directories).

2. repodiff.py

Description: Script to compare two apt repositories, and figure out which packages are new/old

Requirement: Python

Usage: Run ./repodiff.py to see usage.

3. pysshfsplus

Pysshfs is a frontend to sshfs commandline. It's a simple pygtk utility, and does things well. More details at http://www.ad-comp.be/

I added Autofill options (so it remembers what you last used), and fixed an issue where it did not work correctly with ssh-bound hosts. This was sent upstream, but is yet to be updated. Meanwhile anyone who wants these changes, can pick it up from here.

4. Glance

A tiny pygtk utility that makes dictionary lookup simple. Gnome-dictionary is good, but it lacks things like clibboard lookup, prefix/suffix words, etc.

Glance was written to be as simple to use as wordweb on windows. It is a frontend to dict. Once setup, you can,

 * Lookup a word by simply selecting it in browser/text-editor/ebook reader and hitting F7.
 * Hit F7 anytime to launch.
 * Search for prefix/suffixed words with *. Ex: *arch, matri*, *morph*
 * Provide definition of the word, etymology (along with meaning of the root words), Similar words, usage, etc. These depend on the dicitonaries installed.

Setup:

Instructions are for Ubuntu. First install dependencies and local dictionary via 

  apt-get install python-gtk2 xsel
  apt-get install dictd dict dict-wn dict-gcide

This installs the Wordnet and the Comprehensive English dictionary. You can also install:

  dict-moby-thesaurus - Largest and most comprehensive thesaurus
  dict-jargon - Jargon definitions
  dict-foldoc - FOLDOC dictionary database
  dict-vera - Dictionary of computer related acronyms
  dict-bouvier - John Bouvier's Law Dictionary for the USA
  dict-devil - A satirical, cynical and irreverent dictionary of common words
  dict-gazetteer - Place names, population and location provided by the U.S. Census Bureau

There are multiple language A -> B dictionaries available as well. To see alla vailable dictionaries, run:
  
  apt-cache search dict | grep ^dict

glance is a single file utility. Copy the file to /usr/local/bin

  sudo cp glance /usr/local/bin

Setup keyboard shortcut F7, Add a custom shortcut for glance. Do this by running gnome-keyboard-properties.

All done. Select a word and press F7 anytime to view in all it's defined glory.


5. sshlist.py

A sshmenu like alternative for appindicator menu. Move file into /usr/local/bin, add it to gnome startup list, and add ssh hosts into ~/.sshlist file. One item per line

