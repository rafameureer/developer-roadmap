# Timestamp

O tipo de dado Timestamp no MongoDB é um tipo especial de dados BSON usado internamente para operações como replicação e shard. Ele consiste em um contador de segundos de 32 bits e um contador ordinal incrementante (também de 32 bits), representando o tempo UTC com precisão de um segundo. Diferentemente do tipo Date, os valores Timestamp no MongoDB são únicos e monotonamente crescentes, tornando-os ideais para rastrear alterações e ordenar eventos.

Acesse os seguintes recursos para saber mais:

- [@official@Timestamp](https://www.mongodb.com/docs/manual/reference/bson-types/#timestamps)
- [@article@Trabalhando com datas](https://www.prisma.io/dataguide/mongodb/working-with-dates)
