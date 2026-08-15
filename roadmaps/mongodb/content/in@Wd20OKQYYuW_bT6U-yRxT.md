# $in

O operador `$in` no MongoDB seleciona documentos onde o valor de um campo corresponde a qualquer valor em um array especificado. Ele fornece correspondência múltipla eficiente de valores sem usar várias condições `$or`. O `$in` suporta todos os tipos de dados BSON e é especialmente útil para filtragem por listas de IDs, categorias ou valores enumerados, oferecendo melhor desempenho em comparação com consultas equivalentes `$or`.

Acesse os seguintes recursos para saber mais:

- [@official@Operadores de Agregação](https://www.mongodb.com/docs/manual/reference/operator/aggregation/)
- [@official@$in](https://www.mongodb.com/docs/manual/reference/operator/aggregation/in/)
