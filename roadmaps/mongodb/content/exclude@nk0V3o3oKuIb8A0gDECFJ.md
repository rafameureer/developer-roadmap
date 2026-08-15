# $exclude

O operador `$exclude` do projeto no MongoDB é usado para excluir explicitamente campos específicos dos resultados da consulta, permitindo que você retorne todos os campos de um documento, exceto aqueles que são explicitamente excluídos. Quando usar `$exclude`, você especifica quais campos omitir definindo-os como 0 ou false no documento de projeção, e todos os outros campos serão incluídos automaticamente no conjunto de resultados. Este operador é particularmente útil quando você deseja recuperar a maioria dos dados de um documento enquanto exclui informações sensíveis como senhas, metadados internos ou campos grandes que não são necessários para uma operação específica, ajudando a reduzir o bandwidth da rede e melhorar o desempenho da consulta transferindo apenas os dados necessários.

Acesse os seguintes recursos para saber mais:

- [@oficial@Incluir ou Excluir Campos em um Índice de Coringa](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-wildcard/create-wildcard-index-multiple-fields/)
- [@oficial@Projetar Campos para Retornar da Consulta](https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/)
