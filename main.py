from src.data_loader import get_stock_price, get_stock_history, get_news
from src.sentiment import analyze_sentiment
import matplotlib.pyplot as plt

def plot_stock_price(ticker, period_days=7):
    """Plot the stock price for the last `period_days` days"""
    data = get_stock_history(ticker, period_days)
    if data is None:
        print("⚠ No historical price data available for plotting.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], marker='o', linestyle='-', color='blue')
    plt.title(f"{ticker} Price Last {period_days} Days")
    plt.xlabel("Date")
    plt.ylabel("Close Price ($)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    print("\n" + "="*40)
    print("      AI MARKET ANALYZER")
    print("="*40 + "\n")

    ticker = input("Enter stock ticker (e.g. NVDA, TSLA, AAPL): ").upper().strip()
    
    try:
        days_input = input("Analysis period in days (default 7): ").strip()
        period_days = int(days_input) if days_input else 7
    except ValueError:
        print("❌ Invalid input. Using default 7 days.")
        period_days = 7

    print(f"\n[1/3] Fetching data for {ticker}...")

    # Get the current stock price
    price = get_stock_price(ticker)
    if price is None:
        print(f"❌ Error: Could not fetch price for {ticker}. Check the ticker.")
        return

    # Get the news for the stock
    raw_news = get_news(ticker)
    if not raw_news:
        print(f"❌ No news available for {ticker} in Yahoo Finance.")
        return

    print(f"📈 Current Price: ${price:.2f}")

    # Plot the stock price for the specified period
    plot_stock_price(ticker, period_days)

    print(f"[2/3] Analyzing news for the last {period_days} days...")

    # Analyze sentiment of the news
    avg_sentiment = analyze_sentiment(raw_news, days=period_days)

    # Print final summary
    print("\n" + "="*40)
    print(f"        FINAL SUMMARY FOR {ticker}")
    print("-"*40)
    print(f"Sentiment Score: {avg_sentiment:.2f}")

    if avg_sentiment > 0.15:
        bias = "BULLISH 📈"
    elif avg_sentiment < -0.15:
        bias = "BEARISH 📉"
    else:
        bias = "NEUTRAL ⚖️"

    print(f"Overall Bias:    {bias}")
    print("="*40 + "\n")

if __name__ == "__main__":
    main()