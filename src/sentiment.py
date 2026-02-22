from transformers import pipeline

def analyze_sentiment(news_list):
    """Analyze the sentiment of a list of news articles.

    Returns the average sentiment score.
    Positive score = bullish, negative score = bearish.
    """
    sentiment_pipeline = pipeline("sentiment-analysis")
    scores = []

    if not news_list:
        print("No news found for this ticker.")
        return 0

    for article in news_list:
        # Extract title from nested 'content', fallback to "No Title"
        title = article.get("content", {}).get("title", "No Title")

        # Run sentiment analysis
        result = sentiment_pipeline(title)[0]

        print(f"\nHeadline: {title}")
        print(f"Sentiment: {result['label']} ({result['score']:.2f})")

        score = result["score"] if result["label"] == "POSITIVE" else -result["score"]
        scores.append(score)

    # Return average sentiment
    return sum(scores) / len(scores) if scores else 0