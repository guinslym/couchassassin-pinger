#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
import time
from random import randint
import os, io
from os import path
import logging
from logging.handlers import RotatingFileHandler

___author__= 'Guinsly Mondesir'

def configuration_of_the_logs():
    """This will serve as a base for logs configuration

    Warning: make sure there is a filename 'logs.txt' inside of
    a folder named 'logs'

    Returns:
        Object -- a logging object
    """
    log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

    #todo:#Check to see if the folder exist
    my_path = path.dirname(path.realpath(__file__))
    logFile = my_path + '/logs/logs.txt'

    #The logs.txt file can't be more than 5MB
    my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024,
                                     backupCount=2, encoding=None, delay=0)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.INFO)

    app_log = logging.getLogger('root')
    #app_log.setLevel(logging.INFO)
    app_log.setLevel(logging.INFO)

    app_log.addHandler(my_handler)
    #app_log.info('configuraring the logs')

    return app_log

app_log = configuration_of_the_logs()

"""
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
"""

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

def how_many_time_to_visit_this_url(url='http://couchassassin.com/event/black-bluegrass-fest-2016'):
    """
    Between each visits
    wait some seconds
    """
    number = randint(1,20)
    app_log.info("==number of visit === " + str(number))
    counter = 0
    for num in range(number):
        visit_url(url)
        seconde = randint(1,181)
        app_log.info("counter : {0}/{1} for {2} sec.".format(counter,number,str(seconde)))
        app_log.info("sleeping for " + str(seconde) + " sec.")
        time.sleep(seconde)
        counter = counter + 1


if __name__ == '__main__':
    today = date.today()
    black_n_bluegrass_fest = date(today.year, 8, 7)
    if today < black_n_bluegrass_fest:
        how_many_time_to_visit_this_url()
