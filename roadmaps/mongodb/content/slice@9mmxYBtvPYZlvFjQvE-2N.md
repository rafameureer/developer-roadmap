# $slice

O operador de projeção `$slice` no MongoDB retorna um subconjunto de elementos de array dos documentos. Ele suporta valores positivos para elementos do início, valores negativos do final e combinações skip/limit para a paginação dentro de arrays. O `$slice` é essencial para gerenciar grandes arrays em documentos, implementar paginação de arrays e reduzir o tráfego de rede retornando apenas as partes necessárias dos arrays.

Acesse os seguintes recursos para saber mais:

- [@official@$slice](https://www.mongodb.com/docs/manual/reference/operator/aggregation/slice/)
- [@article@MongoDB slice - Sintaxe & Exemplos](https://database.guide/mongodb-slice/)
