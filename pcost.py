#pcost.py


##with open('Data/portfolio.csv', 'rt') as f:
##    data = f.read()
##
##    print(data)

'''Now we turn the script into a function. The
function gets called at the bottome of the script.'''

def portfolio_cost(filename):
    with open('Data/portfolio.csv', 'rt') as f:
        a = next(f)
        total = 0
        for line in f:
            row = line.split(',')
            nshares = int(row[1])
            price = float(row[2])
            total += nshares*price
    return total

cost = portfolio_cost('Data/portfolio.csv')

print("Total cost", cost)

    
        
