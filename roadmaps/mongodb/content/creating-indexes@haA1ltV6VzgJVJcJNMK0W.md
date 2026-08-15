# Criando Índices

Criar índices no MongoDB usa o método `createIndex()` para construir estruturas de dados que melhoram a performance das consultas. Índices podem ser criados em campos individuais, múltiplos campos (compósitos) ou com tipos especiais como texto, geoespacial ou hash. Boas práticas incluem analisar padrões de consulta, criar índices antes de importações de grandes volumes de dados e monitorar o uso dos índices para garantir a performance ótima sem sobreíndексação.

Acesse os seguintes recursos para saber mais:

- [@oficial@createIndex](https://www.mongodb.com/docs/manual/reference/method/db.collection.createindex/)
- [@oficial@Consultas Geoespaciais](https://www.mongodb.com/docs/manual/geospatial-queries/)
- [@artigo@Índice Único vs Compósito em MongoDB](https://medium.com/@rakeebnazar/single-vs-compound-mongodb-index-in-depth-analysis-5319cfdd2ce)
