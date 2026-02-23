import yfinance as yf

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    return data["Close"].iloc[-1] if not data.empty else None

def get_news(ticker):
    stock = yf.Ticker(ticker)
    return stock.news if stock.news else []