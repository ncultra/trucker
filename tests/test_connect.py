#!/bin/python


import sys, os, libvirt, pytest
from optparse import OptionParser

sys.path.insert(0, os.path.abspath(os.path.join(os.pardir, "virtutil")))
import libvirtutil 

params=["qemu:///session", "qemu:///system"]

def test_connect():
    for uri in params:
        print uri
        conn = libvirtutil.connect(uri)
        assert conn > 0
        conn.close()
