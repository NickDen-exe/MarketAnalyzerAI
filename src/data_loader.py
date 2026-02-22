import yfinance as yf

def get_stock_price(ticker):
    """Fetch the latest closing price for the given stock ticker."""
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if data.empty:
        return None
    return data["Close"].iloc[-1]

def get_news(ticker, limit=5):
    """Fetch the latest news articles for the given stock ticker."""
    stock = yf.Ticker(ticker)
    return stock.news[:limit] if stock.news else []