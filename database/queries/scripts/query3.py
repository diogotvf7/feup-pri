import requests

# Phrase match
def query3():
    response = requests.get(
        "http://localhost:8983/solr/stocks/select",
        params={
            "q": "title:\"stock market\"~2",
            "indent": "true",
            "q.op": "OR"
        }
    )

    return response