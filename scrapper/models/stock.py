import json

class Stock:
    def __init__(self, **kwargs):
        self.stock_data = {
            "Stock Title": None,
            "Live Price": None,
            "Price Change": None,
            "Price Change Percentage": None,
            "Previous Close": None,
            "Open": None,
            "Bid": None,
            "Ask": None,
            "Day's Range": None,
            "52 Week Range": None,
            "Volume": None,
            "Average Volume": None,
            "Market Cap (intraday)": None,
            "Beta (5Y Monthly)": None,
            "PE Ratio (TTM)": None,
            "EPS (TTM)": None,
            "Earnings Date": None,
            "Forward Dividend & Yield": None,
            "Ex-Dividend Date": None,
            "1y Target Est": None
        }

        for key, value in kwargs.items():
            if key in self.stock_data:
                self.stock_data[key] = value
            else:
                raise ValueError(f"'{key}' is not a valid stock attribute.")
            
    def dump(self):
        return json.dumps(self.__dict__)
            

            
