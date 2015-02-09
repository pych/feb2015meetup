# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 20:14:29 2015

@author: akandavelu
"""

import os
import time

sin, sout, serr = os.popen3('ps -ef ')

while 1:
    print sout.read()
    print serr.read()
    time.sleep(10)
