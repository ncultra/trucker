#!/bin/python

import sys, os, libvirt, argparse
import pool

class volume:
    def __init__(self, pool, name, config_file):
        self.conn = conn
        self.config_file = config_file
        self.pool = pool
        self.name = name
        self.libvirt_vol = None
        try:
            f = open(self.config_file, 'r')
# TODO: limit file len with config, only read up to len bytes
            self.config = f.read(1024)
            f.close()
        except IOError, e:
            print e.errno
            print os.strerror(e.errno)

    def __vol_exists__():
        pool.refresh()
        for n in pool.listAllVolumes():
            if n == self.name:
                return True
        return False

    def: __create__(self):
        if self.libvirt_vol != None:
            raise(IOError, 'libvirt volume already exists in storage pool')
        self.libvirt_vol = pool.createXML(self.config)
        # TODO: hack to ensure the name is consistent with self and libvirt
        self.name = self.libvirt_pool.name()
        return self.libvirt_vol
    
            
    def open(self):
        """
        Create a libvirt volume if it does not exist, return the libvirt volume.
        """
        if self.__vol_exists__():
            pool.refresh()
            for v in self.pool.listAllVolumes:
                if self.name == v.name():
                    self.libvirt_vol = v
        else:
            self.libvirt_vol  = self.__create__()

   def clone(self, config):
       """
       Clone this libvirt volume and return the clone
       """
       # pool.createXMLFrom - create a volume by cloning ande existing volume
