# report.py

'''opens a portfolio and reads the data into a list
of dictionaries. Then defines another function that
makes a dictionary of prices for more stocks.'''

import csv

portfolio = []

def read_portfolio(filename):

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            holding = dict(zip(headers, holding))
            portfolio.append(holding)

    return portfolio



def read_prices(filename):
    '''Read the prices into a dictionary mapping prices
    to names.'''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)

        for row in rows:
            try:
               prices[row[0]] = float(row[1])
            except IndexError:
                print("got a bad value:", row)
    return prices



if __name__=='__main__':

    portfolio = read_portfolio('Data/portfolio.csv')
    prices    = read_prices('Data/prices.csv')

    
    

    
