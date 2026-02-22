# MarketAnalyzerAI

AI-powered console application that analyzes stock-related news sentiment.

## Overview

MarketAnalyzerAI fetches real-time stock data and recent news, 
then applies NLP sentiment analysis to determine short-term market bias.

## Features

- Real-time stock data via Yahoo Finance
- News extraction
- Sentiment analysis using HuggingFace Transformers
- Aggregated bullish / bearish bias scoring

## Tech Stack

- Python
- yfinance
- transformers (HuggingFace)
- torch
- pandas

## Example Output

===== AI MARKET NEWS ANALYZER =====

Stock: AMD
Current Price: $172.40

Analyzed 5 news articles

Average Sentiment: 0.61
Overall Bias: Bullish

## Future Improvements

- FinBERT integration
- Streamlit dashboard
- Telegram bot
- Historical backtesting
- Sentiment vs price correlation analysis