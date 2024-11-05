#!/bin/bash

# Check if a filename was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <json_filename>"
    exit 1
fi

# Set the JSON filename from the first argument
JSON_FILE="$1"

# Send the request to Solr
curl -X POST -H "Content-Type: application/json" \
"http://localhost:8983/solr/stocks/select" \
-d "@$JSON_FILE"
