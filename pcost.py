#pcost.py

import csv

def portfolio_cost(filename):
    '''computes the total cost of a portfolio'''

    total = 0
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n, row in enumerate(rows, start=1):
            record = dict(zip(headers,row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total += nshares*price
            except ValueError:
                print(f'Row {n}: Bad row: {row}')
    return total




if __name__ == '__main__':

    ##import sys
    ##if len(sys.argv) == 2:
    ##    filename = sys.argv[1]
    ##else:
    ##    filename = input('Enter a filename:')


    filename = 'Data/missing.csv'
    cost = portfolio_cost(filename)
    print('Total cost:', cost)
     
