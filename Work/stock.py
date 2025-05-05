# stock.py
#
# Exercise 4.1

from typedproperty import typedproperty

class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name   = name
        self.shares = shares
        self.price  = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price

    def sell(self, nshares):
        '''
        Sell a number of shares
        '''
        self.shares -= nshares