#!/bin/python

import sys, os, libvirt, argparse

class pool:

    def __init__(self, conn, name, config_file):
        self.conn = conn
        self.config_file = config_file
# TODO: read name from config file <name></name>
        self.name = name
        self.libvirt_pool = None
        try:
            f = open(self.config_file, 'r')
# TODO: limit file len with config, only read up to len bytes
            self.config = f.read(1024)
            f.close()
        except IOError, e:
            print e.errno
            print os.strerror(e.errno)

# TODO: should this return the actual libvirt pool object?
    def create(self):
        if self.libvirt_pool != None:
            raise (IOError, 'libvirt storage pool already exists!')
        self.libvirt_pool = conn.storagePoolCreateXML(self.config)
        return self.libvirt_pool
# is IOError the right exception ?
    def close(self):
        cc = None
        if self.libvirt_pool != None:
            cc = self.libvirt_pool.destroy()
            self.libvirt_pool = None
        if cc:
            raise (IOError, 'failed to close libvirt storage pool.')
        return cc

# returns a list of volume names
    def list(self):
        if self.libvirt_pool != None:
            self.libvirt_pool.refresh()
            return self.libvirt_pool.listVolumes()
        else:
            raise (IOError, "underlying libvirt object is not allocated")

# returns a list of volume objects
    def volumes(self):
        if self.libvirt_pool != None:
            self.libvirt_pool.refresh()
            return self.libvirt_pool.listAllVolumes()
        else:
            raise (IOError, "underlying libvirt object is not allocated")

# return one volume object if it exists

    def get_volume(self, name):
        if self.libvirt_pool != None:
            return self.libvirt_pool.storageVolLookupByName(name)
        else:
            raise (IOError, "underlying libvirt object is not allocated")
    
# test harness
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="%prog --uri host --file xml")
    parser.add_argument('-u', '--uri', default='qemu:///system',
                        help='libvirtd host')
    parser.add_argument('-f', '--file', default='pool.xml',
                        help='xml file describing the storage pool')
    args = parser.parse_args()
    print vars(args)
    uri = vars(args)['uri']
    f =  vars(args)['file']

    conn = libvirt.open(uri)
    pool = pool(conn, 'tpool', f)
    print(pool)

    virt_pool = pool.create()
    print virt_pool
    names =  pool.list()
    print names[0]
    print pool.get_volume(names[0])
    pool.close()