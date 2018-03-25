# report.py

'''opens a portfolio and reads the data into a list
of dictionaries.'''

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




if __name__=='__main__':
    
    portfolio = read_portfolio('Data/portfolio.csv')
    print("Portfolio: ", portfolio)
    
