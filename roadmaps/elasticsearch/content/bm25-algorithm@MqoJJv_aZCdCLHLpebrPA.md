# Algoritmo BM25

BM25 (Best Matching 25) é uma função de classificação usada por motores de busca para estimar a relevância dos documentos em relação a uma consulta específica. É uma função de recuperação de bolsa de palavras que pontua documentos com base nos termos da consulta que aparecem em cada documento, considerando a frequência do termo e o comprimento do documento. O algoritmo ajusta para o comprimento do documento, impedindo que documentos mais longos sejam favoritados injustamente, e também considera como frequentemente um termo aparece na coleção completa de documentos.

Acesse os seguintes recursos para saber mais:

- [@official@Prática BM25 - Parte 1: Como os shards afetam a pontuação de relevância no Elasticsearch](https://www.elastic.co/blog/practical-bm25-part-1-how-shards-affect-relevance-scoring-in-elasticsearch)
- [@official@Prática BM25 — Parte 2: O Algoritmo BM25 e suas variáveis](https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables)
- [@official@Prática BM25 - Parte 3: Considerações para escolher b e k1 no Elasticsearch](https://www.elastic.co/blog/practical-bm25-part-3-considerations-for-picking-b-and-k1-in-elasticsearch)
- [@official@Melhorando a pontuação de texto com o BM25](https://www.elastic.co/elasticon/conf/2016/sf/improved-text-scoring-with-bm25)
- [@article@Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25)
