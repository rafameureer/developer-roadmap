# $skip

A fase de agregação `$skip` pula um número especificado de documentos antes de passar os documentos restantes para a próxima etapa do pipeline. É comumente usado com `$limit` para implementar paginação, permitindo que as aplicações pulam páginas anteriores e recuperem conjuntos específicos de resultados. `$skip` deve ser usado com cuidado com valores grandes de skip, pois pode impactar o desempenho.

Acesse os seguintes recursos para saber mais:

- [@official@$skip](https://www.mongodb.com/docs/manual/reference/operator/aggregation/skip/)
- [@article@MongoDB Skip Documents - Sintaxe & Exemplos ](https://www.tutorialkart.com/mongodb/mongodb-skip-documents/)
