docker stop meic_solr_semantic
docker rm meic_solr_semantic

echo 'Starting server at http://localhost:8982'

docker run -p 8983:8982 --name meic_solr_semantic -v ${PWD}:/data -d solr:9 solr-precreate stocks
sleep 10

docker cp schemas/my_synonyms.txt meic_solr_semantic:/var/solr/data/stocks/conf
sleep 3


curl -X POST -H 'Content-type:application/json' --data-binary @schemas/semantic/schema_semantic_2.json http://localhost:8982/solr/stocks/schema

sleep 3
curl -X POST -H 'Content-type:application/json' \--data-binary @data/semantic/data_semantic_2.json \http://localhost:8982/solr/stocks/update?commit=true
