#stock.py

'''initialize the class with the class inheriting from
the object class if there is no other parent.'''
class Stock(object):
    '''An instance of a stock holding consisting of a name,
    number of shares and the price.'''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares*self.price

    def sell(self, nshares):
        self.shares -= nshares



    
