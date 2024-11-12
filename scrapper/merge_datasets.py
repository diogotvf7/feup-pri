import pandas as pd
import json

article_json_path = "./database/article.json"
article_df = pd.read_json(article_json_path)

stock_json_path = "./database/stock.json"
stock_df = pd.read_json(stock_json_path)

article_df['created_at'] = pd.to_datetime(article_df['created_at'])
stock_df['date'] = pd.to_datetime(stock_df['date'])

merged_data = []

date_mapping = {
    '2024-10-10T00:00:00.000Z' : ['22/10/2024', '12/10/2024', '02/11/2024', '04/11/2024'],
    '2024-10-11T00:00:00.000Z' : ['22/10/2024', '12/10/2024', '02/11/2024', '04/11/2024'],
    '2024-10-12T00:00:00.000Z' : ['02/11/2024', '22/10/2024', '12/10/2024', '04/11/2024'],
    '2024-10-18T00:00:00.000Z' : ['02/11/2024', '22/10/2024', '04/11/2024'],
    '2024-10-19T00:00:00.000Z' : ['02/11/2024', '22/10/2024', '04/11/2024'],
    '2024-10-20T00:00:00.000Z' : ['02/11/2024', '22/10/2024', '04/11/2024'],
    '2024-10-21T00:00:00.000Z' : ['02/11/2024', '22/10/2024', '04/11/2024'],
    '2024-10-22T00:00:00.000Z': ['02/11/2024', '04/11/2024'],
    '2024-11-01T00:00:00.000Z': ['02/11/2024', '04/11/2024'],
    '2024-11-02T00:00:00.000Z' : ['02/11/2024', '04/11/2024'],
    '2024-11-04T00:00:00.000Z' : ['12/11/2024'],
    '2024-11-05T00:00:00.000Z' : ['12/11/2024'],
    '2024-11-06T00:00:00.000Z' : ['12/11/2024'],
    '2024-11-07T00:00:00.000Z' : ['12/11/2024'],
    '2024-11-08T00:00:00.000Z' : ['12/11/2024'],
    '2024-11-09T00:00:00.000Z' : ['12/11/2024'],
    '2024-11-10T00:00:00.000Z' : ['12/11/2024'],
    '2024-11-11T00:00:00.000Z' : ['12/11/2024'],
    '2024-11-12T00:00:00.000Z' : ['12/11/2024'],
}

for _, article_row in article_df.iterrows():
    article_date = article_row['created_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    
    merged_row = {
        "title": article_row['title'],
        "authors": article_row['authors'],
        "created_at": article_date,
        "body": article_row['body'],
        "stocks_changes_name": [],  
        "stocks_changes_value": []  
    }

    try:
        stock_names = article_row['stocks_changes_name'] if len(article_row['stocks_changes_name']) > 0 else []
    except TypeError:
        print("Type error")
    
    for stock_name in stock_names:
        target_date = date_mapping.get(article_date)

        if target_date:
            if isinstance(target_date, str):
                target_date = [target_date]

            for date in target_date:
                matching_stock = stock_df[
                    (stock_df['Stock'] == stock_name) & 
                    (stock_df['date'] == date)
                ]
                
                if not matching_stock.empty:
                    price_change_percentage = matching_stock['Price Change Percentage'].values[0]
                    merged_row['stocks_changes_name'].append(stock_name)
                    merged_row['stocks_changes_value'].append(price_change_percentage)
                    break

    merged_data.append(merged_row)

output_json_path = './database/merged_output.json'
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(merged_data, json_file, indent=4, ensure_ascii=False)

