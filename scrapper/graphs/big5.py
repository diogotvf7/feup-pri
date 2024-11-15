import json
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from collections import defaultdict

with open('database/stock.json', 'r') as file:
    data = json.load(file)

stock_data = defaultdict(list)
for entry in data:
    stock_data[entry["Stock"]].append({
        "Date": pd.to_datetime(entry["date"], format="%d/%m/%Y"),
        "Open": float(entry["Open"].replace(",", "")),
        "High": float(entry["Days Top"].replace(",", "")),
        "Low": float(entry["Days Bottom"].replace(",", "")),
        "Close": float(entry["Live Price"].replace(",", "")),
        "Volume": int(entry["Volume"].replace(",", ""))
    })

selected_stocks = ["MSFT", "AAPL", "TSLA", "NVDA", "AMZN"]

plt.rc('axes', labelsize=12)   
plt.rc('xtick', labelsize=10)  
plt.rc('ytick', labelsize=10)  
plt.rc('figure', titlesize=16) 

fig, axes = plt.subplots(len(selected_stocks), 1, figsize=(10, 12), sharex=True)
fig.suptitle("Stock Price Evolution - Candlestick Charts", fontsize=18) 

for i, stock in enumerate(selected_stocks):
    if stock in stock_data:
        df = pd.DataFrame(stock_data[stock])
        df.set_index("Date", inplace=True)
        df.sort_index(inplace=True)
        mpf.plot(
            df,
            type="candle",
            ax=axes[i],
            style="charles",
            ylabel=stock,
            mav=(5, 10),  
            volume=False  
        )
        axes[i].set_ylabel(stock, fontsize=14)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("big5.png")
plt.show()
