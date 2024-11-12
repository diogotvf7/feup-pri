import json

article_json_path = "./database/article.json"
with open(article_json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

for article in data:
    stocks_changes_name = []
    stocks_changes_value = []

    if "stocks_changes" in article:
        for stock_change in article["stocks_changes"]:
            stocks_changes_name.append(stock_change["name"])
            stocks_changes_value.append(stock_change["value"])

        article["stocks_changes_name"] = stocks_changes_name
        article["stocks_changes_value"] = stocks_changes_value

        article.pop("stocks_changes", None)
    elif (("stocks_changes" not in article) and ("stocks_changes_name" not in article) and ("stocks_changes_value" not in article)):
        article["stocks_changes_name"] = stocks_changes_name
        article["stocks_changes_value"] = stocks_changes_value


with open(article_json_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Article JSON has been updated with separate stocks_changes_name and stocks_changes_value lists.")
