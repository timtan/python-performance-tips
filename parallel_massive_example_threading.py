#!/bin/env python
# Copyright (c) 2009 Denis Bilenko. See LICENSE for details.

"""Spawn multiple workers and wait for them to complete"""

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']
urls *= 5

import threading
import Queue
queue = Queue.Queue()

import urllib2

def print_head(url):
        print 'Starting %s' % url
        data = urllib2.urlopen(url).read()
        print '%s: %s bytes: %r' % (url, len(data), data[:50])

def print_head_thread():
    while True:
        url = queue.get()
        print_head(url)
        queue.task_done()


for i in range(15):
    t = threading.Thread(target=print_head_thread)
    t.setDaemon(True)
    t.start()

for url in urls:
    queue.put(url)
queue.join()

print "finish"
