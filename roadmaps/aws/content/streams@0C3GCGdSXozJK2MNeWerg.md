# Streams

O AWS DynamoDB Streams é uma sequência ordenada em tempo real de modificações a nível de item em qualquer tabela do DynamoDB. Quando você ativa um stream em uma tabela, o DynamoDB captura informações sobre todas as modificações aos itens de dados na tabela. As alterações são registradas em tempo real e podem ser configuradas para disparar funções Lambda do AWS imediatamente após ocorrer um evento. Com DynamoDB Streams, as aplicações podem acessar esse log e visualizar as modificação de dados na ordem em que ocorreram. O stream registra modificações de dados a nível de item como `Insert`, `Modify` e `Remove`. Cada registro do stream é então organizado em um tipo de exibição de stream, onde as aplicações podem acessar até 24 horas de histórico de modificação de dados.

Acesse os seguintes recursos para saber mais:

- [@oficial@Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html)
