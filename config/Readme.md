./scripts/query_solr.py --query config/query1/query1_simple_schema.json --uri http://localhost:8983/solr --collection stocks | \
./scripts/solr2trec.py > config/query1/result_query1_simple_schema.txt
