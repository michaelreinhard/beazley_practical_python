#pcost.py

import csv
import fileparse

def portfolio_cost(filename):
    '''computes the total cost of a portfolio'''

    total = 0
    records = fileparse.parse_csv(filename, select=['shares', 'price'],
              types=[int,float], has_headers=True,
              delimiter=',', silence_errors=False)

    for record in records:
        total += record['shares']*record['price']

    return total




if __name__ == '__main__':

    ##import sys
    ##if len(sys.argv) == 2:
    ##    filename = sys.argv[1]
    ##else:
    ##    filename = input('Enter a filename:')


    filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print('Total cost:', cost)
     
