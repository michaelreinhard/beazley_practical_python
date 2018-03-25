#pcost.py

import csv

def portfolio_cost(filename):
    '''computes the total cost of a portfolio'''

    total = 0
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n, row in enumerate(rows):
            try:
                nshares = int(row[1])
                price = float(row[2])
                total += nshares*price
            except ValueError:
                print(f'Row {n}: Bad row: {row}')
    return total


import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
    
        
