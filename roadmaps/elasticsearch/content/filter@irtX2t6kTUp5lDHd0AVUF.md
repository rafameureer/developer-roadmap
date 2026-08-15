# Contexto de Filtro Booliano

O contexto `filter` em uma consulta Booliana no Elasticsearch é usado para reduzir os documentos que correspondem a uma consulta sem afetar a pontuação de relevância. É como um pré-filtro que eficientemente exclui documentos que não atendem a critérios específicos antes do processo de pontuação começar, tornando-o ideal para correspondências exatas, consultas de intervalo e outras condições onde a relevância não é um fator.

Acesse os seguintes recursos para saber mais:

- [@official@Consulta Booliana](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-bool-query)
- [@official@Perdido na Tradução: Operações Booleanas e Filtros na Consulta Booliana](https://www.elastic.co/blog/lost-in-translation-boolean-operations-and-filters-in-the-bool-query)
- [@video@Consulta Booliana no Elasticsearch (Should & Cláusulas Filter) - S1E14: Mini Aula Inicial Rápida](https://www.youtube.com/watch?v=Uh1F2lezIfY)
- [@video@Consulta Booliana no Elasticsearch | Bool, Filter, Must, Must Not, Should, DSL | ES7 para Iniciantes #4.3](https://www.youtube.com/watch?v=ba2Qn3y486M)
