# pcost.py
#
# Exercise 1.27

import csv
from report import read_portfolio
import sys

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename) 
    return sum([ s['shares']*s['price'] for s in portfolio ])

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)