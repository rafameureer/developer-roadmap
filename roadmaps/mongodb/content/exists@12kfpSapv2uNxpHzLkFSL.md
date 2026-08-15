# $exists

O operador `$exists` no MongoDB corresponde a documentos com base na presença ou ausência de um campo especificado. Quando definido como `true`, ele encontra documentos que contêm o campo, independentemente do valor (incluindo `null`), e quando `false`, encontra documentos que faltam completamente o campo. O `$exists` é útil para validação de esquema, verificações de qualidade dos dados e filtragem de documentos com campos opcionais.

Acesse os seguintes recursos para saber mais:

- [@official@$exists](https://www.mongodb.com/docs/manual/reference/operator/query/exists/)
- [@article@Operador $exists do MongoDB](https://sparkbyexamples.com/mongodb/using-mongodb-exists-operator/)
