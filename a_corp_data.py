# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 19:20:01 2016

@author: Francisco
"""
from os import listdir
from os.path import isfile, join
from xml.dom.minidom import parse, parseString
from xml.dom import minidom
import numpy as np
import pandas as pd
import csv
import os

asset_type_file = "final_database_corp.pkl"
p_data = pd.read_pickle(asset_type_file)
cfo_td = [pd.to_numeric(p_data[p_data['RATING'] == i]['CFO/TD']).mean() for i in range(1,10)]
td_ebitda = [pd.to_numeric(p_data[p_data['RATING'] == i]['TD/EBITDA']).mean() for i in range(1,10)]
ebitda_ie = [pd.to_numeric(p_data[p_data['RATING'] == i]['EBITDA/IE']).mean() for i in range(1,10)]
ebitda_marg = [pd.to_numeric(p_data[p_data['RATING'] == i]['EBITDA_marg']).mean() for i in range(1,10)]
td_tc = [pd.to_numeric(p_data[p_data['RATING'] == i]['TD/TC']).mean() for i in range(1,10)]

fnum_isin = p_data['ISIN'].drop_duplicates().values.shape[0]
ax_rat = ['AAA','AA','A','BBB','BB','B','CCC','CC','D']
x_axis = list(range(1,10))

plt.xticks(x_axis, ax_rat)
plt.plot(x_axis,cfo_td, 'ro')
plt.show()

plt.xticks(x_axis, ax_rat)
plt.plot(x_axis,td_ebitda, 'ro')
plt.show()

plt.xticks(x_axis, ax_rat)
plt.plot(x_axis,ebitda_ie, 'ro')
plt.show()

plt.xticks(x_axis, ax_rat)
plt.plot(x_axis,ebitda_marg, 'ro')
plt.show()

plt.xticks(x_axis, ax_rat)
plt.plot(x_axis,td_tc, 'ro')
plt.show()