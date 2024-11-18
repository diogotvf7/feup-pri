import requests

def query2():
    response = requests.get(
        "http://localhost:8983/solr/stocks/select",
        params={
            "defType": "edismax",
            "qf": "title^3 body^2 authors",
            "pf": "title^3 author^2 body",
            "indent": "true",
            "q.op": "AND",
            "sort": "created_at desc",
            "q": "Apple stock forecast",
        }
    )
    return response.json()


if __name__ == "__main__":
    response = query1()
    print(response.text)