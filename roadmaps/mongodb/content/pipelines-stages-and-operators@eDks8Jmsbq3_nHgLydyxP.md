# Pipelines, Stages e Operadores

Os pipelines de agregação no MongoDB são compostos por etapas sequenciais que processam e transformam documentos, onde cada etapa executa uma operação específica usando vários operadores antes de passar os resultados para a próxima etapa. As etapas como `$match` (filtragem), `$group` (agrupamento e agregação), `$project` (seleção e transformação de campos), `$sort` (ordenação), `$lookup` (junções) e `$unwind` (expansão de arrays) podem ser combinadas em qualquer ordem para criar fluxos de trabalho complexos de processamento de dados. Os operadores dentro dessas etapas incluem operadores aritméticos ($add, $multiply), operadores de comparação ($eq, $gt), operadores de array ($push, $addToSet), operadores de data ($dateToString, $year) e operadores condicionais ($cond, $ifNull), fornecendo um framework poderoso e flexível para análise de dados, relatórios e operações ETL diretamente no banco de dados.

Acesse os seguintes recursos para saber mais:

- [@oficial@Pipeline de Agregação](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)
- [@oficial@Etapas de Agregação](https://www.mongodb.com/docs/manual/reference/operator/aggregation-pipeline/)
- [@oficial@$project](https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/)
- [@oficial@$group](https://www.mongodb.com/docs/manual/reference/operator/aggregation/group/)
