# Indexação em Lote

A indexação em lote no Elasticsearch é uma maneira de enviar várias operações de indexação, atualização ou exclusão para o cluster do Elasticsearch em uma única solicitação. Em vez de enviar cada documento individualmente, você os agrupa juntos, que reduz significativamente a sobrecarga da comunicação de rede e do processamento, resultando em velocidades de indexação mais rápidas. Esse método é particularmente útil quando lidando com grandes conjuntos de dados ou quando precisar ingestir dados rapidamente.

Acesse os seguintes recursos para saber mais:

- [@oficial@Indexação em lote ou exclusão de documentos](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-bulk)
- [@artigo@Ajuste para velocidade de indexação](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/indexing-speed)
- [@artigo@Como Indexar Documentos do Elasticsearch com a API de Indexação em Lote em Python](http://towardsdatascience.com/how-to-index-elasticsearch-documents-with-the-bulk-api-in-python-b5bb01ed3824/)
- [@artigo@Otimizando a Indexação em Lote do Elasticsearch para Alto Desempenho](https://opster.com/guides/elasticsearch/how-tos/optimizing-elasticsearch-bulk-indexing-high-performance/)
- [@vídeo@Api de Indexação em Lote para Múltiplos Documentos e Modificações [ElasticSearch 7 para Iniciantes #3.3]](https://www.youtube.com/watch?v=6IYkfn9me-w)
