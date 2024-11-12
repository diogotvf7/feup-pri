import requests

# Independent boost
def query2():
    response = requests.get(
        "http://localhost:8983/solr/stocks/select",
        params={
            "q": "*:*",
            "boost": "{!boost b=recip(ms(NOW,created_at),3.16e-11,1,1)}", # Boost based on recency
            "indent": "true",
            "q.op": "OR"
        }
    )
    return response