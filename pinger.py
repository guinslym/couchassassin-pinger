#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
import time

___author__= 'Guinsly Mondesir'

def visit_url(url):
    """
    visit an url
    """
    try:
        import urllib2
        response = urllib2.urlopen(url)
        html = response.read()
    except:
        import urllib3
        http = urllib3.PoolManager()
        html = http.request('GET', url)
    print(html)

def how_many_time_to_visit_this_url():
    """
    Between each visits
    wait some seconds
    """
    from random import randint
    number = randint(1,20)
    print("number of visit " + str(number))
    for num in range(number):
        url = 'http://couchassassin.com/event/black-bluegrass-fest-2016'
        visit_url(url)
        seconde = randint(1,25)
        print("sleeping for " + str(seconde) + "sec.")
        time.sleep(seconde)


if __name__ == '__main__':
    today = date.today()
    black_n_bluegrass_fest = date(today.year, 8, 7)
    if today < black_n_bluegrass_fest:
        how_many_time_to_visit_this_url()
