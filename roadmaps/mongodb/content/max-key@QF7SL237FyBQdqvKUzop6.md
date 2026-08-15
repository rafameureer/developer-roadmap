# Max Key

MaxKey é o oposto de MinKey no MongoDB, representando o maior valor possível para um campo. Ele é considerado ser maior que todos os outros valores do banco de dados. O MaxKey é particularmente útil em cenários onde você precisa definir um limite superior em consultas ou operações de classificação. Por exemplo, ao procurar documentos com um campo que seja menor que um determinado valor, usar MaxKey permite incluir todos os documentos, pois ele atua como o maior valor possível.

Acesse os seguintes recursos para saber mais:

- [@official@Índices Multicampos](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-multikey/)
- [@article@Classe MaxKey](https://mongodb.github.io/node-mongodb-native/4.2/classes/MaxKey.html)
- [@article@Exemplo de max() e min() no MongoDB](https://examples.javacodegeeks.com/software-development/mongodb/mongodb-max-and-min-example/)
