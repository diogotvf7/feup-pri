import requests

# Proximity
def query4():
    response = requests.get(
        "http://localhost:8983/solr/stocks/select",
        params={
            "q": "\"stock market\"~5",
            "indent": "true",
            "q.op": "OR"
        }
    )

    return response