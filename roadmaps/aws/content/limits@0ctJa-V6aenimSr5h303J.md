# Limite

Em termos de DynamoDB, é importante estar ciente de determinados limites. Existem dois tipos de modos de capacidade - provisionado e a pedido, com diferentes unidades de capacidade de leitura/gravação. Você tem controle sobre a alocação da taxa de transferência para operações de leitura/gravação. No entanto, há um limite máximo de 40000 unidades de capacidade de leitura e 40000 unidades de capacidade de gravação no modo a pedido por tabela. É também importante notar que o valor da chave de partição e o valor da chave de classificação podem ser um máximo de 2048 bytes e 1024 bytes, respectivamente. Cada item, incluindo a chave primária, pode ter um tamanho máximo de 400KB. A capacidade provisionada total para todas as tabelas e índices secundários globais em uma região não deve ultrapassar 20.000 unidades de capacidade de gravação e 20.000 unidades de capacidade de leitura no modo a pedido. Lembre-se, você pode solicitar aumentar esses limites entrando em contato com o suporte do AWS.

Acesse os seguintes recursos para saber mais:

- [@oficial@Configurações de Limite](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html)
