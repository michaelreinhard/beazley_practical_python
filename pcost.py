#pcost.py

import report

def portfolio_cost(filename):
    '''computes the total cost of a portfolio'''

    portfolio = report.read_portfolio(filename)

    return sum([stock['shares']*stock['price'] for stock in portfolio])


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s datafile' % args[0])
    filename = args[1]
    print('Total cost:' , portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)
