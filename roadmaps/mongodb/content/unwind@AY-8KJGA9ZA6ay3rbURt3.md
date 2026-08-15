# $unwind

A etapa de agregação `$unwind` desmonta campos de array, criando documentos separados para cada elemento do array. É essencial para processar documentos com arrays incorporados ao achatá-los em registros individuais. O `$unwind` suporta opções para preservar arrays nulos/vazios e incluir índices de array, permitindo uma análise detalhada de estruturas de dados baseadas em arrays e fluxos de normalização.

Acesse os seguintes recursos para saber mais:

- [@official@$unwind](https://www.mongodb.com/docs/manual/reference/operator/aggregation/unwind/)
- [@article@Técnicas Avançadas com MongoDB: Dominando Lookup](https://medium.com/@akshatgupta1903/advanced-techniques-with-mongodb-mastering-lookup-and-unwind-acfc8a8ad5b9)
