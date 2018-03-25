##report.py

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
    report_data = []
    headers = ('Name', 'Shares', 'Price', 'Change')
    report_data.append(headers)
    for s in portfolio:
        current_value = s['shares']*prices[s['name']]
        s['current_value'] = current_value
        t = (s['name'], s['shares'], s['price'],s['current_value']) 
        report_data.append(t)
    return report_data




if __name__=='__main__':

    portfolio = read_portfolio('Data/portfolio.csv')
    prices    = read_prices('Data/prices.csv')
    report = make_report_data(portfolio, prices)
    print(f'%10s %10s %10s %10s' % report[0])
    print(('-' * 10 + ' ') * 4)
    for r in report[1:]:
        print('%10s %10d %10.2f %10.2f' % r)
    
    


