import requests

def query4():

    response = requests.get(
        "http://localhost:8983/solr/stocks/select",
        params={
            "defType": "edismax",
            "qf": "title^3 body^2 authors",
            "pf": "title^3 author^2 body",
            "indent": "true",
            "q.op": "OR",
            "sort":"created_at desc",

            "q": "Why has NVIDIA stock skyrocketed in the past month?",
        }
    )

    return response

if __name__ == "__main__":
    response = query4()
    print(response.text)