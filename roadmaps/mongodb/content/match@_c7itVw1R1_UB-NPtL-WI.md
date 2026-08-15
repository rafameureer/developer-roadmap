# $match

O estágio `$match` da agregação filtra documentos na pipeline, semelhante à operação de consulta find(). Deve ser colocado cedo na pipeline para reduzir o número de documentos e melhorar o desempenho. O `$match` suporta todos os operadores de consulta e pode usar índices quando posicionado no início da pipeline, tornando-o essencial para filtragem eficiente de dados em workflows de agregação.

Acesse os seguintes recursos para saber mais:

- [@official@$match](https://www.mongodb.com/docs/manual/reference/operator/aggregation/match/)
- [@official@Operadores de Agregação](https://www.mongodb.com/docs/manual/reference/operator/aggregation/)
- [@article@Como usar match dentro de lookup na agregação Mongo](https://medium.com/@arashramy/how-to-use-match-inside-lookup-in-mongo-aggregation-2431a8920ec6)
