# Min Key

O MinKey é um valor especial no MongoDB que representa o menor valor possível para um campo. Ele é considerado ser menor do que todos os outros valores na base de dados. Isso torna o MinKey útil em consultas e operações de classificação onde você deseja estabelecer uma faixa inferior. Por exemplo, ao pesquisar documentos com um campo maior que um certo valor, você pode usar o MinKey para garantir que todos os documentos sejam incluídos, pois ele efetivamente atua como o menor valor possível.

Acesse os seguintes recursos para saber mais:

- [@official@Índices Multi-chave](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-multikey/)
- [@article@Classe MinKey](https://mongodb.github.io/node-mongodb-native/4.2/classes/MinKey.html)
- [@article@Exemplo de max() e min() no MongoDB](https://examples.javacodegeeks.com/software-development/mongodb/mongodb-max-and-min-example/)
