import requests

# Term boost
def query5():
    response = requests.get(
        "http://localhost:8983/solr/stocks/select",
        params={
            "q": "title:stock^2.0 AND body:market^1.0",
            "indent": "true",
            "q.op": "OR"
        }
    )

    return response
