import json
import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_scores(title, body):
    combined_text = f"{title} {body}"
    return analyzer.polarity_scores(combined_text)

def add_sentiment_to_entries(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    for entry in data:
        title = entry.get('title', '')
        body = entry.get('body', '')
        
        sentiment_scores = get_sentiment_scores(title, body)
        
        entry['sentiment_compound'] = sentiment_scores['compound']
        
    with open('database/data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def removePercentage(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    for entry in data:
        if 'stocks_changes_value' in entry and isinstance(entry['stocks_changes_value'], list):
            for i in range(len(entry['stocks_changes_value'])):
                if isinstance(entry['stocks_changes_value'][i], str) and entry['stocks_changes_value'][i].endswith('%'):
                    entry['stocks_changes_value'][i] = entry['stocks_changes_value'][i][:-1]  # Remove the '%' character
    
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


add_sentiment_to_entries('database/merged_output.json')
removePercentage('database/data.json')
