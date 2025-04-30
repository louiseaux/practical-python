# report.py
#
# Exercise 2.4

from fileparse import parse_csv
from stock import Stock

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''  
    with open(filename, 'rt') as lines:
        portdicts = parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
    
    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename, 'rt') as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))

def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []

    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        summary = (s.name, s.shares, current_price, change)
        report.append(summary)
    return report

def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)


def portfolio_report(portfolio_filename, prices_filename):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Generate the report data
    report = make_report(portfolio, prices)

    # Print it out
    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile')
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)