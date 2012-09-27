#!/bin/env python
# Copyright (c) 2009 Denis Bilenko. See LICENSE for details.

"""Spawn multiple workers and wait for them to complete"""

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']
urls *= 5

import multiprocessing

import urllib2

def print_head(url):
        print 'Starting %s' % url
        data = urllib2.urlopen(url).read()
        print '%s: %s bytes: %r' % (url, len(data), data[:50])

pool = multiprocessing.Pool(10)
pool.map(print_head, urls)

print "finish"
