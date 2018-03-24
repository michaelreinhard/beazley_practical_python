#pcost.py


##with open('Data/portfolio.csv', 'rt') as f:
##    data = f.read()
##
##    print(data)

'''A better way to read in a file is to take advantage
of the fact it has lines.'''

with open('Data/portfolio.csv', 'rt') as f:
    a = next(f)
    total = 0
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        total += nshares*price

print("Total cost", total)

    
        
