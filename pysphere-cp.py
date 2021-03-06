#!/usr/bin/env python
""" Connects to vsphere and prints out lists of VMs that are registered with
that VSPhere host"""

import pysphere
import argparse 
import sys
import getpass

groups = ["prod", "dev", "acc", "unknown"]
vb03 = 'vdc02vmvc03.vdc.cpr.ca'
vb04 = 'vdc02vmvc01.vdc.cpr.ca'
vb05 = 'vdc01vmvc05.vdc.cpr.ca'

#vb06 = 'vdc01vmvc06.vdc.cpr.ca' # DR
vb07 = 'vdc02vmvc05.vdc.cpr.ca'
vb08 = 'vdc02vmvc04.vdc.cpr.ca'
vblocks = {'vb03' : vb03,
        'vb04' : vb04,
        'vb05' : vb05,
        'vb07' : vb07,
        'vb08' : vb08 }

dev_linux_vms = []
prod_linux_vms = []
acc_linux_vms = []
unknown_linux_vms = []



def server_connect(host, username, password):
    """Connects to VSPhere, will prompt for the password"""
    server = pysphere.VIServer()
    try:
        server.connect(host, username, password)
    except Exception as error:
        print(("Could not connect to vCenter: %s as %s - %s") % 
                (host, username, error))

    return server

def print_list(env):
    if args.debug:
        print "printing env is %s" % env
    """ Logic to print out the list of VMs in the various lists"""
    if env ==  'dev':
        if args.debug:
            print "# %s VMs on %s" % (env, host)
        for i in dev_linux_vms:
            print i
    elif env == 'acc':
        if args.debug:
            print "# %s VMs on %s" % (env, host)
        for i in acc_linux_vms:
            print i
    elif env == 'prod':
        if args.debug:
            print "# %s VMs on %s" % (env, host)
        for i in prod_linux_vms:
            print i
    elif env == 'unknown':
        if args.debug:
            print "# %s VMs on %s" % (env, host)
        for i in unknown_linux_vms:
            print i
    else:
        for group in groups:
            print_list(group)


def get_vm_list(host, username, env):
    """ Builds some lists with virtual machine names it gets from vsphere.
    Filters based on the hostname. Upon completion calls print list. Might have
    to move the print_list(env) call out of here later on."""
    server = server_connect(host, username, password)
    vms = server.get_registered_vms()
    if args.debug:
        print "Building list of linux VMs. Please wait!"
    for vm in vms:

        virtual_machine = server.get_vm_by_path(vm)
        vmname = virtual_machine.get_property('name')
        if vmname[0] is 'l' or vmname[0] is 'L':
            if vmname[4] is 'd' or vmname[4] is 'D':
                dev_linux_vms.append(vmname)

            elif vmname[4] is 'a' or vmname[4] is 'A':
                acc_linux_vms.append(vmname)
            elif vmname[4] is 'p' or vmname[4] is 'P':
                prod_linux_vms.append(vmname)
            else:
                unknown_linux_vms.append(vmname)
    if args.debug:
        print "running print_list(%s)" % env
    print_list(env)

def do_all_vblocks(username, env):
    for vblock in vblocks:
        get_vm_list(vblock, username, env)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', help='fqdn of vsphere server',
            action='store', required='True')
    parser.add_argument('-u', '--username', help='your vsphere username',
            action='store', required='True')
    parser.add_argument('-p', '--password', help='your vsphere password',
            action='store')
    parser.add_argument('-l', '--list', help='List all guest VMs', 
            action='store_true')
    parser.add_argument('-e', '--env', 
            help="Print specific env e.g. (dev, acc, prod,unknown, all)",
            action="store")
    parser.add_argument('-g', '--guest', help='Print a single guest', 
            action='store')
    parser.add_argument('-n', '--no-ssl-verify', 
        help="Do not do SSL Cert Validation", action='store_true')
    parser.add_argument('-d', '--debug',
            help="Print extra output for debugging purposes",
            action='store_true')

    args = parser.parse_args()
    if args.password:
        password = args.password
    else:
        password = getpass.getpass()


    if args.no_ssl_verify is True:
        """ allows disabling of SSL Cert verification"""
        import ssl

        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            # Legacy Python that doesn't verify HTTPS certificates by default
            pass
        else:
            # Handle target environment that doesn't support HTTPS verification
            ssl._create_default_https_context = _create_unverified_https_context

    host = args.server
    username = args.username

    if host == 'all':
        if args.debug:
            print 'running args.server all'
        if args.env:
            env = args.env
            do_all_vblocks(username, env)
    elif args.env:
        if args.debug:
            print "list env is: %s" % args.env
        env = args.env
        get_vm_list(host, username, env)

    elif args.list:
        args.env = "all"
        if args.debug:
            print "list all is: %s" % args.env
        get_vm_list(host, username, args.env)

    else:
        parser.print_help()
        sys.exit(1)
 

# vim: tabstop=4 shiftwidth=4 expandtab filetype=python
