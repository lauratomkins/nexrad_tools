# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:03:52 2019

@author: lmtomkin
"""

import nexradaws

date = '20191210'
radar = 'KOKX'

conn = nexradaws.NexradAwsInterface()

availscans = conn.get_avail_scans(date[0:4], date[4:6], date[6:8], radar)

results = conn.download(availscans, 'C:\\Users\\lmtomkin\\Documents\\winter_storms\\data\\NEXRAD\\'+radar+'\\'+date)
