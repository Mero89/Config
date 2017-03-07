# coding=utf-8

import os
import sys
import datetime as dt
import pandas as pd

os.chdir('/Users/mero/Desktop')
dir_list = ['/Users/mero/Projects/medius',
            '/Users/mero/Projects/PricerMO',
            '/Users/mero/Projects/SKope', '/Users/mero/Projects']
            
sys.path.extend(dir_list)

from minerva.validators import to_date, to_pip, to_yield
