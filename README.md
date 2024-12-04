I'm trying to replicate what I do in this script:

_____________________
docker stop meic_solr
docker rm meic_solr

echo 'Starting server at http://localhost:8983'

docker run -p 8983:8983 --name meic_solr -v ${PWD}:/data -d solr:9 solr-precreate stocks
sleep 10

docker cp my_synonyms.txt meic_solr:/var/solr/data/stocks/conf
sleep 3


curl -X POST -H 'Content-type:application/json' --data-binary @schema_simple.json http://localhost:8983/solr/stocks/schema

sleep 3
curl -X POST -H 'Content-type:application/json' \--data-binary @data.json \http://localhost:8983/solr/stocks/update?commit=true
__________________

But with a docker-compose.yml file.
This is what I have written so far:

