##report.py

'''opens a portfolio and reads the data into a list
of dictionaries. Then defines another function that
makes a dictionary of prices for more stocks.'''

import csv
import fileparse
import stock
import tableformat

def read_portfolio(filename):
    '''Read a stock portfolio into a list of dictionaries
    with keys name, shares, and price.'''

    portdicts = fileparse.parse_csv(filename,
                                    select=['name','shares','price'],
                                    types=[str,int,float])

    portfolio = [stock.Stock(d['name'], d['shares'], d['price'])
                 for d in portdicts]

    return portfolio


def read_prices(filename):
    '''Read the prices into a stock object with price
    and name attributes.'''

    #set has_headers=False and apply dict function to tuples
    pricedict = dict(fileparse.parse_csv(filename, types=[str,float],
                                 has_headers=False))
    return pricedict
                


def make_report_data(portfolio, prices):
    '''
    Generate list of tuples showing the
    (name, shares, price, change) given a portfolio
    list and a prices dictionary.
    '''
    report_data = []
    for stock in portfolio:

        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        report_data.append(summary)

    return report_data

'''Change is just the change in the price. So Price is
the purchase price and Change in the current price minus
the purchase price.'''

def print_report(report, formatter):
    '''
    Print a nicely formatted table with headers
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

    
def portfolio_report(portfolio_data, prices_data, fmt='txt'):
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
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

#to make it run on command line
def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfoliofile, pricefile' % args[0])
    portfolio_report(args[1], args[2], args[3])



if __name__=='__main__':
    import sys
    main(sys.argv)


    


