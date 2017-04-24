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

nodes = '/Users/Carnec/Desktop/Business_Analytics/analyticalbusinessmodelling/assignment3/coordinates5.csv'
with open(nodes, 'r') as f:
    csvreader = csv.reader(f,delimiter = ',')
    i = 0
    for row in csvreader:
        df.loc[i] = [row[1],row[3],row[4]]
        i+=1
        
        
matrix = df.as_matrix() 
dfdist = pd.DataFrame(columns=('City1', 'City2', 'Distance')) 

size = len(matrix)
s = (size+1,size+1)
distmatrix = np.zeros(s)
i=0
for i in range(size):
    distmatrix[0][i] = str(matrix[i][0])

dfdist2 = pd.DataFrame(columns=[df['City']]) 
  
    
    
#l=0   
#for j in range(len(matrix)):
#    for k in range(len(matrix)):
#        l = l+1
##        print(vincenty((matrix[j][1],matrix[j][2]),(matrix[k][1],matrix[k][2])))
#        dfdist.loc[l] = [matrix[j][0],matrix[k][0],vincenty((matrix[j][1],matrix[j][2]),(matrix[k][1],matrix[k][2])).km]
#        