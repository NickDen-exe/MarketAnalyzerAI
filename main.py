from src.data_loader import get_stock_price, get_news
from src.sentiment import analyze_sentiment

def main():
    print("===== AI MARKET NEWS ANALYZER =====\n")

    ticker = input("Enter stock ticker (e.g. AMD, NVDA, SPY): ").upper()

    # Fetch stock price
    price = get_stock_price(ticker)
    if price is None:
        print(f"Could not fetch price for {ticker}.")
        return

    # Fetch news articles
    news = get_news(ticker)
    print(f"\nCurrent Price of {ticker}: ${price:.2f}")
    print(f"Analyzing {len(news)} news articles...")

    # Analyze sentiment
    avg_sentiment = analyze_sentiment(news)

    # Display final sentiment
    print("\n===== FINAL SENTIMENT SCORE =====")
    print(f"Average Sentiment: {avg_sentiment:.2f}")

    if avg_sentiment > 0.2:
        print("Overall Bias: Bullish 📈")
    elif avg_sentiment < -0.2:
        print("Overall Bias: Bearish 📉")
    else:
        print("Overall Bias: Neutral ⚖️")

if __name__ == "__main__":
    main()