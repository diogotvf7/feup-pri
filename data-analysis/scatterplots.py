import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
import os

# Paths to JSON files
stock_json_path = "./database/stock.json"
article_json_path = "./database/article.json"

# Read article JSON data
article_df = pd.read_json(article_json_path)
stock_df = pd.read_json(stock_json_path)

stock_df['Live Price'] = stock_df['Live Price'].astype(str).str.replace(',', '').astype(float)
stock_df['52 Week Bottom'] = stock_df['52 Week Bottom'].astype(str).str.replace(',', '').astype(float)
stock_df['52 Week Top'] = stock_df['52 Week Top'].astype(str).str.replace(',', '').astype(float)
stock_df['Volume'] = stock_df['Volume'].astype(str).str.replace(',', '').astype(float)


# summary = stock_df.describe()  # Include all columns, even non-numeric ones
# print("Summary Statistics:\n", summary)



##  Live Price vs 52 Week Range for Selected Stocks'

relevant_stocks = ['MRO', 'AUR', 'FHN']  # Example stocks
filtered_stock_df = stock_df[stock_df['Stock'].isin(relevant_stocks)]

# Summary Statistics
summary = filtered_stock_df.describe()  # Include all columns, even non-numeric ones
print("Summary Statistics:\n", summary)

# Plot
plt.figure(figsize=(10, 6))
plt.bar(filtered_stock_df['Stock'], 
         filtered_stock_df['52 Week Top'] - filtered_stock_df['52 Week Bottom'], 
         bottom=filtered_stock_df['52 Week Bottom'], 
         color='lightgray', label='52 Week Range')
plt.scatter(filtered_stock_df['Stock'], 
            filtered_stock_df['Live Price'], 
            color='red', label='Live Price', s=100)  # Increased size for visibility

plt.xlabel('Stock')
plt.ylabel('Price ($)')
plt.title('Live Price vs 52 Week Range for Selected Stocks')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save the plot instead of showing it
output_folder = "graphs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

plt.savefig(os.path.join(output_folder, "live_price.png"))
plt.close()  



## Price to Movement plot 
## 3 with highest ratio and 3 with lowest


stock_df['Price Movement'] = stock_df['Live Price'] - stock_df['Previous Close']

# Calculate Volume-to-Price Movement Ratio
stock_df['Volume to Price Movement Ratio'] = stock_df['Volume'] / stock_df['Price Movement']

# Filter out any rows where Price Movement is zero to avoid division errors
stock_df = stock_df[stock_df['Price Movement'] != 0]

# Get the top 3 and bottom 3 stocks based on the Volume-to-Price Movement Ratio
top_stocks = stock_df.nlargest(3, 'Volume to Price Movement Ratio')
bottom_stocks = stock_df.nsmallest(3, 'Volume to Price Movement Ratio')

# Combine the results
selected_stocks = pd.concat([top_stocks, bottom_stocks])

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(selected_stocks['Volume'], selected_stocks['Price Movement'], color='blue')

for i in range(len(selected_stocks)):
    plt.annotate(selected_stocks['Stock'].iloc[i], 
                 (selected_stocks['Volume'].iloc[i], selected_stocks['Price Movement'].iloc[i]),
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')

plt.xlabel('Volume')
plt.ylabel('Price Movement ($)')
plt.title('Volume vs Price Movement for Selected Stocks')
plt.grid(True)
plt.tight_layout()

# Save the plot
output_folder = "graphs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

plt.savefig(os.path.join(output_folder, "volume_vs_price_movement.png"))
plt.close()



# authors_list = []
# stock_changes_list = []

# # Open article JSON file
# with open(article_json_path, 'r') as f:
#     data = json.load(f)

# # Extract relevant data from the raw JSON
# for entry in data:
#     authors = entry['authors'] 
    
#     # Check if 'stocks_changes' key exists in the entry and skip if not
#     if 'stocks_changes' in entry and entry['stocks_changes']:
#         stock_changes = entry['stocks_changes']
        
#         # For each stock change, associate it with each author
#         for change in stock_changes:
#             stock_value = float(change['value'].replace('%', ''))  # Convert percentage to float
#             for author in authors:
#                 authors_list.append(author)
#                 stock_changes_list.append(stock_value)

# # Check if we have any valid data to plot
# if authors_list and stock_changes_list:
#     # Create a DataFrame
#     df = pd.DataFrame({
#         'Author': authors_list,
#         'Stock Change (%)': stock_changes_list
#     })

#     # Create scatter plot
#     plt.figure(figsize=(10, 6))
#     plt.scatter(df['Author'], df['Stock Change (%)'], alpha=0.6)

#     plt.xlabel('Authors')
#     plt.ylabel('Stock Change (%)')
#     plt.title('Scatter Plot of Authors vs Stock Changes')
#     plt.xticks(rotation=45)
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()
# else:
#     print("No valid data to plot.")
