import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from collections import defaultdict
import numpy as np
from matplotlib.lines import Line2D

with open('database/stock.json', 'r') as file:
    data = json.load(file)

dates = sorted(["12/10/2024", "22/10/2024", "02/11/2024", "04/11/2024", "12/11/2024"])
prices_by_date = defaultdict(list)
for entry in data:
    live_price = float(entry["Live Price"].replace(",", ""))
    prices_by_date[entry["date"]].append(live_price)

dates = sorted(prices_by_date.keys())
min_prices = [min(prices_by_date[date]) for date in dates]
max_prices = [max(prices_by_date[date]) for date in dates]
avg_prices = [sum(prices_by_date[date]) / len(prices_by_date[date]) for date in dates]

fig, ax = plt.subplots(figsize=(10, 6))
for i, (date, avg, min_val, max_val) in enumerate(zip(dates, avg_prices, min_prices, max_prices)):
    ax.plot([i, i], [min_val, max_val], color='black', linewidth=1.5)
    ax.plot(i, avg, 'o', color='black', markersize=8)
    ax.plot(i, min_val, 'o', color='blue', markersize=6)
    ax.plot(i, max_val, 'o', color='red', markersize=6)

ax.set_xticks(range(len(dates)))
ax.set_xticklabels(dates, rotation=45, ha="right", fontsize=12)

legend_elements = [
    Line2D([0], [0], marker='o', color='black', label='Average', markersize=8),
    Line2D([0], [0], marker='o', color='blue', label='Min', markersize=6),
    Line2D([0], [0], marker='o', color='red', label='Max', markersize=6)
]
ax.legend(handles=legend_elements, loc="upper right", fontsize=12)

ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Price in USD', fontsize=14)
ax.set_title('Avg-Max-Min Live Prices for Stock Prices', fontsize=16)

y_min = min(min_prices) * 0.95  
y_max = max(max_prices) * 1.05  
ax.set_ylim(y_min, y_max)

plt.tight_layout()
plt.savefig("maxMinAvg.png")
plt.show()
