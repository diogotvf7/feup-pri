import pandas as pd

stock_json_path = "../database/stock.json"
article_json_path = "../database/article.json"

article_df = pd.read_json(article_json_path)
stock_df = pd.read_json(stock_json_path)

print(article_df.head()['stocks_changes'])