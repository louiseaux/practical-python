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

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    
    return prices

def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []

    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        report.append(summary)
    return report

# Read data files and create the report data  
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Generate the report data
report = make_report(portfolio, prices)

# Output the report
for r in report:
    print(r)

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['price']*s['shares']

print(f'Total cost {total_cost:0.2f}')

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += prices[s['name']]*s['shares']

print(f'Current value {total_value:0.2f}')
print(f'Gain/loss {total_value - total_cost:0.2f}')