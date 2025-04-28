# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            stock = {
                    'name' : row[0],
                    'shares' : int(row[1]),
                    'price' : float(row[2])
            }
            portfolio.append(stock)
        
    return portfolio