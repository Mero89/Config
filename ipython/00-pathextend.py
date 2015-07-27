# coding=utf-8

import os
import sys
import datetime as dt

# os.chdir('/Users/mar/Desktop/pylab/scripts')
os.chdir('/Users/mar/PycharmProjects/Medius')
sys.path.extend(['/Users/mar/PycharmProjects/Medius'])

import Medius
import pandas as pd
from PyQt4 import QtGui, QtCore
from Medius.utils import *
from Medius.dal.Models import *
from Medius.lib.Courbe import Courbe
