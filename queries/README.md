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
cat ./queries/query4/qrels/qrels.txt | ./scripts/qrels2trec.py > ./queries/query4/qrels/qrels_trec.txt
```

# Obter resultados

```sh
./src/trec_eval/trec_eval ./queries/query4/qrels/qrels_trec.txt ./queries/query4/qrels/results_simple_trec.txt > ./queries/query4/results/results_simple.txt &&
./src/trec_eval/trec_eval ./queries/query4/qrels/qrels_trec.txt ./queries/query4/qrels/results_complex_trec.txt > ./queries/query4/results/results_complex.txt &&
./src/trec_eval/trec_eval ./queries/query4/qrels/qrels_trec.txt ./queries/query4/qrels/results_opt_trec.txt > ./queries/query4/results/results_opt.txt &&
./src/trec_eval/trec_eval ./queries/query4/qrels/qrels_trec.txt ./queries/query4/qrels/results_semantic_trec.txt > ./queries/query4/results/results_semantic.txt &&
./src/trec_eval/trec_eval ./queries/query4/qrels/qrels_trec.txt ./queries/query4/qrels/results_semantic_2_trec.txt > ./queries/query4/results/results_semantic_2.txt
```


## Generate plots

```sh
cat ./queries/query4/qrels/results_simple_trec.txt | ./scripts/plot_pr.py --qrels ./queries/query4/qrels/qrels_trec.txt --output ./queries/query4/results/results_simple.png &&
cat ./queries/query4/qrels/results_complex_trec.txt | ./scripts/plot_pr.py --qrels ./queries/query4/qrels/qrels_trec.txt --output ./queries/query4/results/results_complex.png &&
cat ./queries/query4/qrels/results_opt_trec.txt | ./scripts/plot_pr.py --qrels ./queries/query4/qrels/qrels_trec.txt --output ./queries/query4/results/results_opt.png &&
cat ./queries/query4/qrels/results_semantic_trec.txt | ./scripts/plot_pr.py --qrels ./queries/query4/qrels/qrels_trec.txt --output ./queries/query4/results/results_semantic.png &&
cat ./queries/query4/qrels/results_semantic_2_trec.txt | ./scripts/plot_pr.py --qrels ./queries/query4/qrels/qrels_trec.txt --output ./queries/query4/results/results_semantic_2.png
```

qrels (merge simple + complexo)
qrels_trec ficam os do qrels que ficaram a 1 em modo trec
