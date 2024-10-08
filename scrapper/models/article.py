#from stock_change import StockChange

class Article:
    def __init__(self, title, created_at, body, stocks_changes=None , authors = None):
        self.title = title
        self.created_at = created_at
        self.body = body
        self.stocks_changes = stocks_changes
        self.author = authors

    
    def to_dict(self):
        filtered_dict = {
            'title': self.title,
            'authors': self.author,
            'created_at': self.created_at,
            'body': self.body,
            'stocks_changes': self.stocks_changes
        }
        return {key: value for key, value in filtered_dict.items() if value is not None}
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.created_at}\nBody: {self.body}\nStocks Changes: {self.stocks_changes}"