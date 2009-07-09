#!/usr/bin/env python

# "British deaths in Iraq and Afghanistan"
# http://www.guardian.co.uk/news/datablog/2009/mar/01/iraq-afghanistan

# British fatalities
# http://spreadsheets.google.com/ccc?key=phNtm3LmDZEOjtESRY5o0dw
# Civilian fatalities
# http://www.iraqbodycount.org/database/download/ibc-individuals

import csv
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
# ['k10271-nw1253', ' Harth Hassan Kazami', 'adult', 'male', 'unknown', 'unknown', '22 Apr 2008', '22 Apr 2008', 'Harithiya, west Baghdad']
start = False
for line in cv:
    if len(line) and line[0] == 'IBC code':
        start = True
        continue
    if start == False:
        continue
    year = int(line[6][-4:])
    cv_per_year[year] = cv_per_year.get(year, 0) + 1
