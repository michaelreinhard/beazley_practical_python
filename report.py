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
                continue
    return prices

def make_report_data(portfolio, prices):
    for s in portfolio:
        current_value = s['shares']*prices[s['name']]
        s['current_value'] = current_value

    return portfolio




if __name__=='__main__':

    portfolio = read_portfolio('Data/portfolio.csv')
    prices    = read_prices('Data/prices.csv')
    report = make_report_data(portfolio, prices)
    print(report)
    
    

    
