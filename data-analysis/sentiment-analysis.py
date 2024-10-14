import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load the article and stock data
article_json_path = "./database/article.json"
article_df = pd.read_json(article_json_path)

stock_json_path = "./database/stock.json"
stock_df = pd.read_json(stock_json_path)

# Make sure the 'stocks_changes' field in article_df contains valid stock names/tickers
article_df['stock_name'] = article_df['stocks_changes'].apply(
    lambda x: x[0]['name'] if isinstance(x, list) and len(x) == 1 else None
)

article_df = article_df.dropna(subset=['stock_name'])
article_df.drop('stocks_changes', axis='columns', inplace=True)

article_df['stock_change'] = stock_df['Price Change Percentage'].apply(
    lambda x: float(x.replace('%', '').replace('+', '')) if isinstance(x, str) else None
)
article_df = article_df.dropna(subset=['stock_change'])

print(article_df.head())

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to get sentiment scores from title and body
def get_sentiment_scores(title, body):
    combined_text = f"{title} {body}"
    return analyzer.polarity_scores(combined_text)

# Apply sentiment analysis to articles
article_df[['neg', 'neu', 'pos', 'compound']] = article_df.apply(
    lambda x: pd.Series(get_sentiment_scores(x['title'], x['body'])), axis=1
)

# Calculate correlation between sentiment scores and stock changes
correlation_results = {}
for sentiment in ['neg', 'neu', 'pos', 'compound']:
    correlation, _ = pearsonr(article_df[sentiment], article_df['stock_change'])
    correlation_results[sentiment] = correlation

# Print correlation results
print("Correlation between sentiment scores and stock changes:")
for sentiment, corr in correlation_results.items():
    print(f"{sentiment}: {corr:.4f}")


# Plot Negative Sentiment vs Stock Change
plt.figure(figsize=(10, 8))
sns.scatterplot(x='neg', y='stock_change', data=article_df)
plt.title('Sentiment Score (Negative) vs Stock Change')
plt.xlabel('Negative Sentiment Score')
plt.ylabel('Stock Change (%)')
plt.grid()
plt.show()

# Plot Positive Sentiment vs Stock Change
plt.figure(figsize=(10, 8))
sns.scatterplot(x='pos', y='stock_change', data=article_df)
plt.title('Sentiment Score (Positive) vs Stock Change')
plt.xlabel('Positive Sentiment Score')
plt.ylabel('Stock Change (%)')
plt.grid()
plt.show()


# Plot Compound Sentiment vs Stock Change
plt.figure(figsize=(10, 8))
sns.scatterplot(x='compound', y='stock_change', data=article_df)
plt.title('Sentiment Score (Compound) vs Stock Change')
plt.xlabel('Compound Sentiment Score')
plt.ylabel('Stock Change (%)')
plt.grid()
plt.show()
