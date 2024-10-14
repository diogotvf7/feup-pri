from datetime import datetime


def format_earnings_date(date_string):
    date_object = datetime.strptime(date_string, "%b %d, %Y")
    formatted_date = date_object.strftime("%d/%m/%Y")
    return formatted_date

def split_stock_title(stock_title):
    last_open_paren_index = stock_title.rfind('(')
    
    if last_open_paren_index == -1 or last_open_paren_index == 0:
        return stock_title, ''
    
    title = stock_title[:last_open_paren_index].strip() 
    stock_symbol = stock_title[last_open_paren_index + 1:].replace(")", "").strip()  
    
    return title, stock_symbol

class Stock:
    def __init__(self, **kwargs):
        self.stock_data = {
            "Stock": None,
            "Stock Title": None,
            "Live Price": None,
            "Price Change": None,
            "Price Change Percentage": None,
            "Previous Close": None,
            "Open": None,
            "Bid": None,
            "Ask": None,
            "Days Range Bottom": None,  
            "Days Range Top": None,     
            "52 Week Bottom": None,
            "52 Week Top": None,
            "Volume": None,
            "Average Volume": None,
            "Market Cap (intraday)": None,
            "Beta (5Y Monthly)": None,
            "PE Ratio (TTM)": None,
            "EPS (TTM)": None,
            "Earnings Date Beginning": None,
            "Earning Date End": None,
            "Forward Dividend & Yield": None,
            "Ex-Dividend Date": None,
            "1y Target Est": None,
            "date": datetime.now().strftime("%d/%m/%Y")
        }

        for key, value in kwargs.items():
            if key == "Price Change Percentage":
                self.stock_data["Price Change Percentage"] = value.replace("(", "").replace(")", "")
            elif key == "Day's Range":
                range_values = value.split(" - ")
                self.stock_data["Days Bottom"] = range_values[0]
                if(len(range_values) == 2):
                    self.stock_data["Days Top"] = range_values[1]
            elif key == "52 Week Range":
                range_values = value.split(" - ")
                self.stock_data["52 Week Bottom"] = range_values[0]
                if(len(range_values) == 2):
                    self.stock_data["52 Week Top"] = range_values[1]
            elif key == "Earnings Date":
                range_values = value.split(" - ")
                self.stock_data["Earnings Date Beginning"] = format_earnings_date(range_values[0])
                if(len(range_values) == 2):
                    self.stock_data["Earning Date End"] = format_earnings_date(range_values[1])
            elif key == "Ex-Dividend Date":
                self.stock_data["Ex-Dividend Date"] = format_earnings_date(value)
            elif key == "Stock Title":
                title, stock_symbol = split_stock_title(value)
                self.stock_data["Stock"] = stock_symbol
                self.stock_data["Stock Title"] = title
            elif key in self.stock_data:
                self.stock_data[key] = value
            else:
                raise ValueError(f"'{key}' is not a valid stock attribute.")
            
    def to_dict(self):
        filtered_dict = {key: value for key, value in self.stock_data.items() if value is not None}
        return filtered_dict
            
