#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path
import requests
from sentence_transformers import SentenceTransformer


def text_to_embedding(text):
    """
    Convert the given text into an embedding using the SentenceTransformer model.
    
    Arguments:
    - text: The text to convert to an embedding.

    Output:
    - A string representing the embedding in the expected format for Solr.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(text, convert_to_tensor=False).tolist()

    # Convert the embedding to the expected format
    embedding_str = "[" + ",".join(map(str, embedding)) + "]"
    return embedding_str


def solr_knn_query(endpoint, collection, embedding):
    url = f"{endpoint}/{collection}/select"

    data = {
        "q": f"{{!knn f=vector topK=12}}{embedding}",
        "fl": "id,text",
        "rows": 12,
        "wt": "json"
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()




def print_results_to_stdout(results):
    """
    Print the search results to standard output in JSON format.

    Arguments:
    - results: The JSON results returned from Solr.
    """
    json.dump(results, sys.stdout, indent=2)
    print()  # Ensure there is a newline after the JSON output


def main():
    # Set up argument parsing for the command-line interface
    parser = argparse.ArgumentParser(
        description="Query Solr using a semantic embedding and print results to stdout."
    )

    # Add arguments for the query text, Solr URI, collection name
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="The text query to search for in Solr."
    )
    parser.add_argument(
        "--uri",
        type=str,
        default="http://localhost:8983/solr",
        help="The URI of the Solr instance (default: http://localhost:8983/solr)."
    )
    parser.add_argument(
        "--collection",
        type=str,
        default="stocks",
        help="Name of the Solr collection to query (default: 'stocks')."
    )

    # Parse command-line arguments
    args = parser.parse_args()

    # Convert the query text to an embedding
    embedding = text_to_embedding(args.query)

    # Perform the Solr k-NN query using the embedding
    results = solr_knn_query(args.uri, args.collection, embedding)

    # Print the results to standard output
    print_results_to_stdout(results)


if __name__ == "__main__":
    main()
