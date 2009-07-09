#!/usr/bin/env python

# "British deaths in Iraq and Afghanistan"
# http://www.guardian.co.uk/news/datablog/2009/mar/01/iraq-afghanistan

# British fatalities
# http://spreadsheets.google.com/ccc?key=phNtm3LmDZEOjtESRY5o0dw
# Civilian fatalities
# http://www.iraqbodycount.org/database/download/ibc-individuals

import csv, numpy
import matplotlib.pyplot as plt

# Extract data

br = csv.reader(open('fm'))
br_per_year = {}
for line in br:
    if len(line) == 0:
        break
    if line[0] == 'YEAR':
        continue
    year = int(line[0])
    deaths = int('0'+line[1])
    if deaths != 0:
        br_per_year[year] = deaths

cv = csv.reader(open('ibc-individuals'))
cv_per_year = {}
start = False
for line in cv:
    if len(line) and line[0] == 'IBC code':
        start = True
        continue
    if start == False:
        continue
    year = int(line[6][-4:])
    cv_per_year[year] = cv_per_year.get(year, 0) + 1

# Plot graph

cvTotals = [cv_per_year[b] for b in sorted(cv_per_year.keys())]
brTotals = [br_per_year[b] for b in sorted(br_per_year.keys())]
ind = numpy.arange(len(cv_per_year.keys()))
width = 0.35

p1 = plt.bar(ind, cvTotals, width, color='r')
p2 = plt.bar(ind, brTotals, width, color='y', bottom=cvTotals)

plt.ylabel('Deaths')
plt.title('Deaths in Iran')
plt.xticks(ind+width/2., sorted(cv_per_year.keys()))
plt.yticks(numpy.arange(0,1500,100))
plt.legend( (p1[0], p2[0]), ('Civilians', 'British soldiers') )

plt.savefig('iraq-deaths.png')
#plt.show()
