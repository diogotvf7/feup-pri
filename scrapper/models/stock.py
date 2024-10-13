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
            "ticker": None,
            "title": None,
            "live_price": None,
            "price_change": None,
            "price_change_percentage": None,
            "previous_close": None,
            "open": None,
            "bid": None,
            "ask": None,
            "days_range_bottom": None,  
            "days_range_top": None,     
            "52_week_bottom": None,
            "52_week_top": None,
            "volume": None,
            "average_volume": None,
            "market_cap_intraday": None,
            "beta_5y_monthly": None,
            "pe_ratio_ttm": None,
            "eps_ttm": None,
            "earnings_date_beginning": None,
            "earning_date_end": None,
            "forward_dividend_and_yield": None,
            "ex_dividend_date": None,
            "1y_target_est": None,
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
            
