import json
#from stock_change import StockChange

class Article:
    def __init__(self, title, author, created_at, body, stocks_changes=None):
        self.title = title
        self.author = author
        self.created_at = created_at
        self.body = body
        self.stocks_changes = stocks_changes
    
    def dump(self):
        return json.dumps(self.__dict__)
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.created_at}\nBody: {self.body}\nStocks Changes: {self.stocks_changes}"