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
    def __pool_exists__(self):
        names = conn.listStoragePools()
        for n in names:
            if n == self.name:
                return True
        return False

    def __create__(self):
        if self.libvirt_pool != None:
            raise (IOError, 'libvirt storage pool already exists!')
        self.libvirt_pool = conn.storagePoolCreateXML(self.config)
        # TODO: hack to ensure the name is consistent with self and libvirt
        self.name = self.libvirt_pool.name()
        return self.libvirt_pool

    def open(self):
        if self.__pool_exists__():
            for p in conn.listAllStoragePools():
                if self.name == p.name():
                    self.libvirt_pool = p
        else:
            self.libvirt_pool = self.__create__()

        return self.libvirt_pool
    
    # TODO: is IOError the right exception here ?
    def delete(self):
        cc = None
        if self.libvirt_pool != None:
            cc = self.libvirt_pool.destroy()
            self.libvirt_pool = None
        if cc:
            raise (IOError, 'failed to close libvirt storage pool.')
        return cc

    def list(self):
        """
        Returns a list of volume names.
        """
        if self.libvirt_pool != None:
            self.libvirt_pool.refresh()
            return self.libvirt_pool.listVolumes()
        else:
            raise (IOError, "underlying libvirt object is not allocated")

    def volumes(self):
        """ 
        Returns a list of volume objects.
        """
        if self.libvirt_pool != None:
            self.libvirt_pool.refresh()
            return self.libvirt_pool.listAllVolumes()
        else:
            raise (IOError, "underlying libvirt object is not allocated")


    def get_volume(self, name):
        """
         Return one volume object if it exists.
        """
        if self.libvirt_pool != None:
            self.libvirt_pool.refresh()
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
    print pool

    virt_pool = pool.open()
    print  pool.list()
    print pool.libvirt_pool.name()
    print pool.name
    pool.delete()
