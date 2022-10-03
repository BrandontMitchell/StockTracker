import yfinance as yf

class StockTracker():
    def __init__(self):
        self.stocks = ["MSFT"]

    def add_stock(self, ticker):
        self.stocks.append(ticker)

    def remove_stock(self, ticker):
        self.stocks.remove(ticker)

    def get_stock(self, ticker):
        return self.stocks[ticker]
    
    def get_stocks(self):
        return self.stocks

    # https://towardsdatascience.com/the-easiest-way-to-pull-stock-data-into-your-python-program-yfinance-82c304ae35dc
    def get_stock_price(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.info['regularMarketPrice']
        
