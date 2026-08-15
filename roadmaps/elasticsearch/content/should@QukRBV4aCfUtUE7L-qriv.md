# Deve Query

A `deve` query é uma consulta booleana que retorna documentos correspondentes a um ou mais de suas sub-consultas. Ela aumenta a pontuação de relevância para cada cláusula correspondente, mas não requer que qualquer cláusula corresponda para um documento ser incluído nos resultados. Se nenhuma outra consulta booleana como `deve` ou `filtrar` estiver presente, pelo menos uma cláusula `deve` deve corresponder.

Acesse os seguintes recursos para saber mais:

- [@oficial@Consulta Booleana](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-bool-query)
- [@artigo@Elasticsearch Query Bool](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-query-bool/)
- [@artigo@Elasticsearch Bool Query - Sintaxe, Exemplo e Dicas](https://pulse.support/kb/elasticsearch-bool-query)
- [@vídeo@Bool Query no Elasticsearch | Bool, Filter, Must, Must Not, Should, DSL | ES7 para Iniciantes #4.3](https://www.youtube.com/watch?v=ba2Qn3y486M)
- [@vídeo@Elasticsearch Bool Query (Cláusulas Should & Filter) - S1E14: Mini Crash Course para Iniciantes](https://www.youtube.com/watch?v=Uh1F2lezIfY)
