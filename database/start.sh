docker stop meic_solr
docker rm meic_solr


docker run -p 8983:8983 --name meic_solr -v ${PWD}:/data -d solr:9 solr-precreate stocks
sleep 10

docker cp my_synonyms.txt meic_solr:/var/solr/data/stocks/conf
sleep 3


curl -X POST -H 'Content-type:application/json' --data-binary @schema.json http://localhost:8983/solr/stocks/schema

sleep 3
curl -X POST -H 'Content-type:application/json' \--data-binary @data.json \http://localhost:8983/solr/stocks/update?commit=true


