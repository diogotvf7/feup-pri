import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import json
from collections import defaultdict

with open('database/data.json', 'r') as file:
    data = json.load(file)

dates = [datetime.strptime(item["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ") for item in data]
sentiment_scores = [item["sentiment_compound"] for item in data]

sentiments_by_date = defaultdict(list)

for date, score in zip(dates, sentiment_scores):
    truncated_date = date.date()
    sentiments_by_date[truncated_date].append(score)

average_sentiments = []
date_labels = []

for date, scores in sorted(sentiments_by_date.items()):
    average_sentiments.append(sum(scores) / len(scores))
    date_labels.append(date)

plt.figure(figsize=(10, 6))

plt.plot(date_labels, average_sentiments, label="Average Sentiment", color='blue', marker='o', linestyle='-', markersize=8)

plt.title('Average Sentiment Scores Over Time', fontsize=16) 
plt.xlabel('Date', fontsize=14)  
plt.ylabel('Average Sentiment Score', fontsize=14)  

plt.xticks(rotation=45, fontsize=12)  
plt.yticks(fontsize=12)  
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

plt.grid(True)
plt.legend(fontsize=12)  

plt.tight_layout()  
plt.savefig("sentimentScoreOverDays.png")
plt.show()
