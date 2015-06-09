#!/bin/python

#import sys, libvirt


import sys, libvirt 
def connect(uri):
    try:
        conn = libvirt.open(uri)
    except:
        print "Failed to open %s" + uri
        sys.exit(1)
    return conn


    
