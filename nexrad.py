# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:03:52 2019

@author: lmtomkin
"""

import matplotlib.pyplot as plt
import tempfile
import pytz
from datetime import datetime
import pyart
import nexradaws

date = '20191203'
radar = 'KOKX'

conn = nexradaws.NexradAwsInterface()

availscans = conn.get_avail_scans(date[0:4], date[4:6], date[6:8], radar)

results = conn.download(availscans, 'C:\\Users\\lmtomkin\\Documents\\winter_storms\\data\\NEXRAD\\'+radar+'\\'+date)
