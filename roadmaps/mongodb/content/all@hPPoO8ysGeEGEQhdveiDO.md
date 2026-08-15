# $all

O operador `$all` no MongoDB seleciona documentos onde um campo de array contém todos os elementos especificados, independentemente da ordem ou dos elementos adicionais. É útil para filtragem baseada em tags e garantir que múltiplos valores obrigatórios existam em arrays. O `$all` realiza correspondência elemento a elemento e pode funcionar com arrays de diferentes tipos de dados, tornando-se essencial para o filtro de arrays multi-critério.

Acesse os seguintes recursos para saber mais:

- [@oficial@Operador $all](https://www.mongodb.com/docs/manual/reference/operator/query/all/)
- [@artigo@$all e $elemMatch no MongoDB](https://dev.to/kawsarkabir/all-and-elemmatch-in-mongodb-4od6)
