# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 07:26:23 2018

@author: ZEN
"""

import time
#from time import strftime

def get_time():

    timeint = [int(time.strftime("%y")),int(time.strftime("%m")),int(time.strftime("%d")),
             int(time.strftime("%H")),int(time.strftime("%M")),int(time.strftime("%S"))]
    timestr = [time.strftime("%y"),time.strftime("%m"),time.strftime("%d"),
             time.strftime("%H"),time.strftime("%M"),time.strftime("%S")]
    timesqlite = time.strftime("20%y-%m-%d %H:%M:%S")
    #timesec = time.time()
    
    return timeint, timestr, timesqlite