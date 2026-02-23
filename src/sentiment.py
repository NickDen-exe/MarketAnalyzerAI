from transformers import BertTokenizer, BertForSequenceClassification, pipeline
from datetime import datetime, timedelta

model_name = "yiyanghkust/finbert-tone"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def analyze_sentiment(news_list, days=7):
    scores = []
    now = datetime.now()
    cutoff_date = now - timedelta(days=days)

    print(f"--- Filtering news since: {cutoff_date.strftime('%Y-%m-%d')} ---")

    for article in news_list:
        pub_time_raw = article.get("providerPublishTime") or article.get("content", {}).get("pubDate")
        
        if isinstance(pub_time_raw, str):
            try:
                pub_date = datetime.strptime(pub_time_raw[:19], '%Y-%m-%dT%H:%M:%S')
            except:
                continue
        elif isinstance(pub_time_raw, (int, float)):
            pub_date = datetime.fromtimestamp(pub_time_raw)
        else:
            continue

        if pub_date < cutoff_date:
            continue

        content = article.get("content", {})
        title = content.get("title") or article.get("title", "")
        summary = content.get("summary") or article.get("summary", "")
        
        full_text = f"{title}. {summary}".strip()
        if len(full_text) < 10:
            continue

        result = sentiment_pipeline(full_text[:512])[0]
        label = result["label"].upper()
        confidence = result["score"]

        score = confidence if "POSITIVE" in label else (-confidence if "NEGATIVE" in label else 0)
        scores.append(score)

        print(f"[{pub_date.strftime('%d-%m %H:%M')}] {title[:60]}... -> {label}")

    if not scores:
        print(f"⚠ No news found for the last {days} days in the analyzed data.")
        return 0

    return sum(scores) / len(scores)