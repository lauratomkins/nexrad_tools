# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:03:52 2019

@author: lmtomkin
"""

import nexradaws
import os

date = '20200218'
radar = 'KBGM'
folder = 'C:\\Users\\lmtomkin\\Documents\\winter_storms\\data\\NEXRAD\\'+radar+'\\'+date

conn = nexradaws.NexradAwsInterface()

availscans = conn.get_avail_scans(date[0:4], date[4:6], date[6:8], radar)

if not os.path.exists(folder):
    os.makedirs(folder)

results = conn.download(availscans, folder)
