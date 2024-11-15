import json
from collections import Counter
import matplotlib.pyplot as plt

with open('database/article.json', 'r') as file:
    data = json.load(file)

company_counter = Counter()
for entry in data:
    companies = entry.get("stocks_changes_name", [])
    company_counter.update(companies)

top_10_companies = company_counter.most_common(10)
print("Top 10 Most Mentioned Companies and Their Counts:")
for i, (company, count) in enumerate(top_10_companies, start=1):
    print(f"{i}. {company}: {count} times")

companies = list(company_counter.keys())
mention_counts = list(company_counter.values())
indices = range(1, len(companies) + 1)  

plt.figure(figsize=(12, 6))

plt.bar(indices, mention_counts, color='skyblue')

plt.xticks(fontsize=14)  
plt.yticks(fontsize=14)  
plt.xlabel("Company Index", fontsize=16)  
plt.ylabel("Number of Mentions", fontsize=16)  
plt.title("Number of Mentions of Each Company", fontsize=18)  

plt.tight_layout()
plt.savefig("companies_mentions.png")
plt.show()
