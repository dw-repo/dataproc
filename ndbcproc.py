# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 13:23:10 2017
 A script to read the data from multible NDBC files, bring the wind up to 10m,
 convert the units and save in csv file
@author: Darbinyan
"""
import gzip
import pandas as pd
import numpy as np


stid = ['41041','46066','46025','46026']
mon = ['01','02','03','04','05','06',]
ye = '2016'

anemhght = [5.,5.,4.,5.]

def isowind(windin,windinav,windinhght,windoutav,windouthght):
    # function to recalculate wind to new averaging period windoutav 
    # on the height windouthght
    c=0.0573*np.sqrt(1.+0.148*windin)
    Iu=0.06*(1.+(0.043*windin))*(np.power(windouthght/windinhght,-0.22))

    windout=windin*(1.+c*np.log(windouthght/windinhght))*(1.-(0.41*Iu*np.log(windoutav/windinav)))
    
    return windout
    


fwin=gzip.open('C:/Users/darbinyan.FSPL/Documents/Personal/ndbc_data/data/46026/46026102016cwind.txt.gz')
fmet=gzip.open('C:/Users/darbinyan.FSPL/Documents/Personal/ndbc_data/data/46026/46026102016stdmet.txt.gz')
datawin = pd.read_table(fwin,sep='\s+',header=[0,1])
datamet = pd.read_table(fmet,sep='\s+',header=[0,1])

wincor = isowind(datawin.get('WSPD').get('m/s'),600,anemhght[3],600,10)

