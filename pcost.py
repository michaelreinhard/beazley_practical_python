#pcost.py

'''Now we turn the script into a function. The
function gets called at the bottome of the script.
We also add a way to catch bad input data and use a
library module.

Remember that the first row is a header and has to
be discarded.'''

import csv

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
##        a = next(f)
        rows = csv.reader(f)
        headers = next(rows)
        total = 0
        for row in rows:
            #split is no longer necessary
##            row = line.split(','))
            try:
                nshares = int(row[1])
                price = float(row[2])
                total += nshares*price
            except ValueError:
                print("Bad line:", row)
    return total


import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
    
        
