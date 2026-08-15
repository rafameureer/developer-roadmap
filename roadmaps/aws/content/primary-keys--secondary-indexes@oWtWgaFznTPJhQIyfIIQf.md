# Chaves Primárias / Índices Secundários

O DynamoDB suporta dois tipos de chaves primárias, que são `Chave de Partição` e `Chave Composta` (Chave de Partição e Chave de Classificação). Uma `Chave de Partição`, também conhecida como chave hash, é uma chave primária simples que tem um valor escalar (uma string, um número ou um blob binário). O DynamoDB usa o valor da chave de partição para distribuir dados em várias partições para desempenho escalonável. Uma `Chave Composta` consiste em dois atributos. O primeiro atributo é a chave de partição, e o segundo atributo é a chave de classificação. O DynamoDB usa a chave de partição para espalhar os dados nas partições e também usa a chave de classificação para armazenar itens em ordem crescente dentro dessas partições. Esta chave de classificação fornece um controle granular adicional sobre a organização dos dados.

Acesse os seguintes recursos para saber mais:

- [@oficial@Chaves Primárias / Índices Secundários](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html)
