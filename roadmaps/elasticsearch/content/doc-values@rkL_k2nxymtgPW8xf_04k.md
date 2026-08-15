# Doc Values

Doc values são uma estrutura de dados no Elasticsearch que armazena valores de campo em um formato orientado a colunas, otimizado para agregações, classificações e scripts. Em vez de armazenar os dados junto com o índice invertido, doc values são armazenados separadamente no disco, tornando-os eficientes para recuperar valores para um grande número de documentos. Isso permite que o Elasticsearch execute operações como classificação e agregação muito mais rápido do que se tivesse que recuperar os dados do índice invertido.

Acesse os seguintes recursos para saber mais:

- [@official@doc_values](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/doc-values)
- [@article@Elasticsearch doc-values-only Fields](https://opster.com/guides/elasticsearch/data-architecture/elasticsearch-doc-values-only-fields/)
- [@article@Elasticsearch _source, doc_values and store Performance](https://sease.io/2021/02/field-retrieval-performance-in-elasticsearch.html)
- [@video@Field Data vs Doc Values | Understanding Elasticsearch Performance Issues](https://www.youtube.com/watch?v=l99lIuvQULk)
