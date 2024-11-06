import requests

# Field boost
def query1():
    response = requests.get(
        "http://localhost:8983/solr/stocks/select",
        params={
            "q": "title:\"stock market\"^2.0 body:\"stock market\"^1.5",
            "indent": "true",
            "q.op": "OR"
        }
    )

    return response