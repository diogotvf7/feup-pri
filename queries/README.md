# Executar a query

coloca no results_simple e no results_complex

```sh
./scripts/query_solr.py --query ./queries/query1/query1_simple.json --uri http://localhost:8983/solr --collection stocks | \
./scripts/solr2trec.py > ./queries/query1/qrels/results_simple_trec.txt
```

```sh
./scripts/query_solr.py --query ./queries/query1/query1_complex.json --uri http://localhost:8983/solr --collection stocks | \
./scripts/solr2trec.py > ./queries/query1/qrels/results_complex_trec.txt
```

# Gerar qrels em formato trec

juntar os dois ficheiros de resultados apenas com os que têm relevância 1 no qrels_trec.txt

```sh
cat ./queries/query1/qrels/qrels.txt | ./scripts/qrels2trec.py > ./queries/query1/qrels/qrels_trec.txt
```

# Obter resultados

```sh
./src/trec_eval/trec_eval ./queries/query1/qrels/qrels_trec.txt ./queries/query1/qrels/results_simple_trec.txt > ./queries/query1/results/results_simple.txt
./src/trec_eval/trec_eval ./queries/query1/qrels/qrels_trec.txt ./queries/query1/qrels/results_complex_trec.txt > ./queries/query1/results/results_complex.txt
```

## Generate plots

```sh
cat ./queries/query1/qrels/results_simple_trec.txt | ./scripts/plot_pr.py --qrels ./queries/query1/qrels/qrels_trec.txt --output ./queries/query1/results/results_simple.png
cat ./queries/query1/qrels/results_complex_trec.txt | ./scripts/plot_pr.py --qrels ./queries/query1/qrels/qrels_trec.txt --output ./queries/query1/results/results_complex.png
```

qrels (merge simple + complexo)
qrels_trec ficam os do qrels que ficaram a 1 em modo trec
