#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:59:43 2017

@author: Carnec
"""

from geopy.distance import vincenty
import numpy as np
import pandas as pd
import csv

df = pd.DataFrame(columns=('City', 'Latitude', 'Longitude'))

nodes = '/Users/Carnec/Desktop/Business_Analytics/analyticalbusinessmodelling/assignment3/coordinates20.csv'
with open(nodes, 'r') as f:
    csvreader = csv.reader(f,delimiter = ',')
    i = 0
    list1 = []
    for row in csvreader:
        list1.append(row[2])
        df.loc[i] = [row[1],row[3],row[4]]
        i+=1
        
        
matrix = df.as_matrix() 
dfdist = pd.DataFrame(columns=('City1', 'City2', 'Distance')) 
step = 0
for j in range(len(matrix)):
    for k in range(len(matrix)):
        dist =  vincenty((matrix[j][1],matrix[j][2]),(matrix[k][1],matrix[k][2])).km
        if dist == float(0):
            pass
        else:
            dfdist.loc[step]=[ matrix[j][0]), matrix[k][0], dist]
            step +=1
  
np.savetxt(r'/Users/Carnec/Desktop/Business_Analytics/analyticalbusinessmodelling/assignment3/distbis.txt', dfdist,delimiter=" ", fmt="%s %s %10.3f")

size = len(matrix)
s = (size+1,size+1)
i=0
#for i in range(size):
#    distmatrix[0][i] = str(matrix[i][0])

dfdist2 = pd.DataFrame(index=[df['City']],columns=[df['City']]) 
for j in range(len(matrix)):
    for k in range(len(matrix)):
        dfdist2[matrix[j][0]][matrix[k][0]] = vincenty((matrix[j][1],matrix[j][2]),(matrix[k][1],matrix[k][2])).km
  
#np.savetxt(r'/Users/Carnec/Desktop/Business_Analytics/analyticalbusinessmodelling/assignment3/dist.txt', dfdist2.values, fmt='%d')
dfdist2.index    
