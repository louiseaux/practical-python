# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                total_cost += shares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print('Bad row:', row)
            
    return total_cost

cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)