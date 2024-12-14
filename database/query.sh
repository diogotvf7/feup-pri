#!/bin/bash

#Check if an integer argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <query_number>"
  exit 1
fi

QUERY_LIST=("Apple stock forecast" "Tesla earnings report" "US election effects on the stock market" "Berkshire Hathaway investments")

QUERY_NUM=$1
QUERY="${QUERY_LIST[$QUERY_NUM-1]}" 
# echo $QUERY

# echo "Starting solr with simple schema"
# ../database/start_simple.sh

# echo -e "\nQuerying Solr with simple query"
# ../scripts/query_solr.py --query ../queries/query$QUERY_NUM/query${QUERY_NUM}_simple.json --uri http://localhost:8983/solr --collection stocks | \
# ../scripts/solr2trec.py > ../queries/query$QUERY_NUM/qrels/results_simple_trec.txt
# echo ola
# echo -e "\nStarting solr with complex schema"
# ../database/start.sh

# echo -e "\nQuerying Solr with complex query"
# ../scripts/query_solr.py --query ../queries/query$QUERY_NUM/query${QUERY_NUM}_complex.json --uri http://localhost:8983/solr --collection stocks | \
# ../scripts/solr2trec.py > ../queries/query$QUERY_NUM/qrels/results_complex_trec.txt

# echo -e "\nQuerying Solr with optimised query"
# ../scripts/query_solr.py --query ../queries/query$QUERY_NUM/query${QUERY_NUM}_opt.json --uri http://localhost:8983/solr --collection stocks | \
# ../scripts/solr2trec.py > ../queries/query$QUERY_NUM/qrels/results_opt_trec.txt

# echo -e "\nStarting solr with semantic schema"
# ../database/start_semantic.sh

# echo -e "\nQuerying Solr with semantic query"
# echo -e "Querying $QUERY"
# python3 ../scripts/query_embedding.py --query "$QUERY" --uri "http://localhost:8983/solr" --collection "stocks"  | \
# python3 ../scripts/solr2trec.py > ../queries/query$QUERY_NUM/qrels/results_semantic_trec.txt


# echo -e "\nStarting solr with semantic schema 2"
# ../database/start_semantic_2.sh

echo -e "\nQuerying Solr with semantic query"
echo -e "Querying $QUERY"
python3 ../scripts/query_embedding.py --query "$QUERY" --uri "http://localhost:8983/solr" --collection "stocks"  | \
python3 ../scripts/solr2trec.py > ../queries/query$QUERY_NUM/qrels/results_semantic_2_trec.txt

