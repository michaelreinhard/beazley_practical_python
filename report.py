##report.py

'''opens a portfolio and reads the data into a list
of dictionaries. Then defines another function that
makes a dictionary of prices for more stocks.'''

import csv
import fileparse


def read_portfolio(filename):
    '''Read a stock portfolio into a list of dictionaries
    with keys name, shares, and price.'''

    return fileparse.parse_csv(filename,
                                    select=['name','shares','price'],
                                    types=[str,int,float])


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
    '''
    Generate list of tuples showing the
    (name, shares, price, change) given a portfolio
    list and a prices dictionary.
    '''
    report_data = []
    for stock in portfolio:

        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        report_data.append(summary)

    return report_data

'''Change is just the change in the price. So Price is
the purchase price and Change in the current price minus
the purchase price.'''

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for r in report[1:]:
        print('%10s %10d %10.2f %10.2f' % r)
    
    
def portfolio_report(portfolio_data, prices_data):
    '''
    make a stock report given the portfolio and
    current prices.
    '''
    #read in data files
    portfolio = read_portfolio(portfolio_data)
    prices = read_prices(prices_data)

    #create report data
    report = make_report_data(portfolio, prices)

    #print out
    print_report(report)

if __name__=='__main__':
    pass

    portfolio_report('Data/portfolio.csv',
                     'Data/prices.csv')


##    portfolio = read_portfolio('Data/portfolio.csv')
##    prices    = read_prices('Data/prices.csv')
##    report = make_report_data(portfolio, prices)
##    print_report(report)

    
    


