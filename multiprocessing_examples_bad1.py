#!/bin/env python
# Copyright (c) 2009 Denis Bilenko. See LICENSE for details.

import multiprocessing,urllib2



def main():
    def print_head(url):
        print 'Starting %s' % url
    urls = ['http://www.google.com',
            'http://www.yandex.ru', ]
    pool = multiprocessing.Pool(10)
    pool.map(print_head, urls)


if __name__ == "__main__" :
    main()