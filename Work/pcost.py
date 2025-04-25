# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            shares = int(row[1])
            price = float(row[2])
            total_cost += shares * price
            
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)