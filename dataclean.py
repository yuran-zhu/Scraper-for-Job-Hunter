# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:39:18 2019

@author: genev
"""

def cleanjobs(jobs):
    import numpy as np
    import pandas as pd
    jobs = jobs[jobs['jobTitle'] != 'None']
    jobs['State'] = jobs['location'].str.split(", ", n = 1, expand = True).iloc[:,1]
    salaryesplit = jobs['salary'].str.split('-', n = 1, expand = True)
    salaryesplit[0] = salaryesplit[0].replace('None', np.nan)
    salaryesplit[1] = salaryesplit[0].replace('None', np.nan)
    salaryesplit = salaryesplit.replace('', np.nan)
    salaryesplit[1] = salaryesplit[1].str.split('(', n = 1, expand = True)[0]
    salaryesplit[1] = salaryesplit[1].str.replace('$','')
    salaryesplit[0] = salaryesplit[0].str.replace('$','')
    salaryesplit[1] = salaryesplit[1].str.replace('k','')
    salaryesplit[0] = salaryesplit[0].str.replace('k','')
    salaryesplit = salaryesplit[~salaryesplit[1].str.contains("Per",na=False)==True]
    jobs['Low Sal'] = salaryesplit[0].astype(float)
    jobs['High Sal'] = salaryesplit[1].astype(float)
    jobs['Average Sal'] = (jobs['Low Sal'] + jobs['High Sal'])/2
    return jobs