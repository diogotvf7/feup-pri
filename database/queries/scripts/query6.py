{
    "query": "title:stoc* AND body:marke~1",
    "params": {
        "indent": "true",
        "q.op": "OR"
    }
}

import requests

# Wildcard
def query6():
    response = requests.get(
        "http://localhost:8983/solr/stocks/select",
        params={
            "q": "title:stoc* AND body:marke~1",
            "indent": "true",
            "q.op": "OR"
        }
    )

    return response