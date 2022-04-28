# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:57:32 2022

@author: Harkiret Singh
"""

import heartpy as hp
import matplotlib.pyplot as plt
import csv
import pandas as pd

        
import pandas as pd
df = pd.read_csv('heartrate_Output_mono.csv')
# If you know the name of the column skip this
first_column = df.columns[0]
# Delete first
df = df.drop([first_column], axis=1)
df.to_csv('heartrate_one_column.csv', index=False)



with open('heartrate_one_column.csv', 'r', newline='') as infile, open('heartrate_normalized.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    rows = list(reader)
    header = rows[0]
    data = rows[1:]

    def div(this_row):
        # I changed it to divide by 1000 
        return [float(this_row[0])/10000]
    new_data = [div(row) for row in data]

    new_rows = [header] + new_data
    for row in new_rows:
        writer.writerow(row)


sample_rate = 250

data = hp.get_data('heartrate_normalized.csv')
#data = hp.get_data('data.csv')

plt.figure(figsize=(12,4))
plt.plot(data)
plt.show()

#run analysis
wd, m = hp.process(data, sample_rate)

#visualise in plot of custom size
plt.figure(figsize=(12,4))
hp.plotter(wd, m)

#display computed measures
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))