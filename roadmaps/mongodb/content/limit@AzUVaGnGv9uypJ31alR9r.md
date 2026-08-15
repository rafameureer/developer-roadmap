# $limit

A etapa de agregação `$limit` restringe o número de documentos passados para a próxima fase no pipeline. É comumente usado com `$sort` para obter os N principais resultados, implementar paginação ou reduzir o overhead de processamento de dados. O `$limit` é eficiente quando combinado com índices e deve ser posicionado estratégicamente no pipeline para minimizar o processamento de documentos em fases subsequentes.

Acesse os seguintes recursos para saber mais:

- [@official@$limit](https://www.mongodb.com/docs/manual/reference/operator/aggregation/limit/)
- [@official@Operadores de Agregação](https://www.mongodb.com/docs/manual/reference/operator/aggregation/)
