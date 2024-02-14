# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    f = open(filename)
    total = 0
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        try:
            cost = int(row[1]) * float(row[2])
            total = total + cost
        except ValueError:
            print("Couldn't parse", row)
    
    return(total)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
