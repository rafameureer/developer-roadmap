# $sort

A fase de agregação `$sort` ordena os documentos por valores de campo especificados em ordem ascendente (1) ou descendente (-1). Ele pode ordenar por múltiplos campos com direções diferentes e suporta a ordenação por valores computados das etapas do pipeline anteriores. Colocar o `$sort` cedo no pipeline pode aproveitar índices para melhor desempenho, enquanto a ordenação tardia se aplica aos resultados agregados.

Acesse os seguintes recursos para saber mais:

- [@official@$sort](https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/)
- [@article@Ordenar Registros: Como Ordenar por Data, Nome e Mais](https://www.prisma.io/dataguide/mongodb/mongodb-sorting)
