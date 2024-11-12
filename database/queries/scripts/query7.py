import requests

# Pesquisa composta
def query7():
    response = requests.get(
        "http://localhost:8983/solr/stocks/select",
        params={
            "q": (
                "title:\"fund\"^2 ",  # Boost for the title containing 'fund'
                "body:\"growth\"^1.5 ",  # Boost for 'growth' in the body field
                "stocks_changes_value:[10 TO *]^3 ",  # Boost for stocks with changes >= 10
                "{!boost b=recip(ms(NOW,created_at),3.16e-11,1,1)}"  # Recency boost for documents based on created_at
            ),
            "indent": "true",
            "q.op": "AND", 
        }
    )

    return response