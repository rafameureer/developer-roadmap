# $include

O operador de projeção `$include` no MongoDB permite que você especifique explicitamente quais campos devem ser incluídos nos resultados da consulta, fornecendo controle preciso sobre os dados retornados do banco de dados. Quando usar o `$include` (ou simplesmente definir campos como 1 ou true em um documento de projeção), apenas os campos especificados e o campo `_id` (a menos que seja explicitamente excluído) estarão presentes nos documentos retornados, o que ajuda a reduzir o tráfego de rede, melhorar o desempenho da consulta e aumentar a segurança limitando a exposição de dados. Esse operador é essencial para otimizar aplicativos que precisam de campos específicos em documentos grandes, especialmente em cenários onde os documentos contêm muitos campos ou objetos aninhados grandes que consumiriam desnecessariamente largura de banda e recursos de processamento.

Acesse os seguintes recursos para saber mais:

- [@official@Projeção de Campos a Retornar dos Resultados da Consulta](https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/)
- [@official@$include](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-wildcard/create-wildcard-index-multiple-fields/)
