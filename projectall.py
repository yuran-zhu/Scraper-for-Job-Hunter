# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:33:35 2019

@author: genev
"""
import scrapping
import dataclean
import visualizedata
import htmloutput

search_job = input('Enter a Job Name: ')
jobs = scrapping.glassdoorscrap(search_job)

indeed_jobs = scrapping.indeedscrpa(search_job)

jobs = dataclean.cleanjobs(jobs)

figstate, figsal = visualizedata.heatmapdraw(jobs, search_job)
salbar_im, salpobar_im, pobar_im = visualizedata.barchartdata(jobs)
text_im = visualizedata.wordclouddata(indeed_jobs)

outdir = 'C:\\Users\\genev\\OneDrive\\Desktop\\Python\\Project'
htmloutput.htmlOutPut(search_job,figstate,figsal,salbar_im,salpobar_im,pobar_im,text_im,outdir)

jobs.to_csv('jobs.csv', index = False) 



