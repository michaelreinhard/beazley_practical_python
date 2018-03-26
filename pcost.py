#pcost.py

import csv
import fileparse

def portfolio_cost(filename):
    '''computes the total cost of a portfolio'''

    records = fileparse.parse_csv(filename, select=['shares', 'price'],
              types=[int,float], has_headers=True,
              delimiter=',', silence_errors=False)


    return sum([record['shares']*record['price'] for record in records])





if __name__ == '__main__':

    ##import sys
    ##if len(sys.argv) == 2:
    ##    filename = sys.argv[1]
    ##else:
    ##    filename = input('Enter a filename:')


    filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print('Total cost:', cost)
     
