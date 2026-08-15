# Índices Compostos

Os índices compostos no MongoDB são construídos em vários campos em uma ordem específica, otimizando consultas que filtram por múltiplos campos. A ordem dos campos é significativamente importante, pois determina quais consultas podem usar eficientemente o índice. Os índices compostos suportam padrões de prefixo, o que significa que eles podem otimizar consultas em qualquer subconjunto à esquerda dos campos indexados, tornando-os versáteis para diversos padrões de consulta.

Acesse os seguintes recursos para saber mais:

- [@oficial@Índices Compostos](https://www.mongodb.com/docs/manual/core/indexes/index-types/index-compound/)
- [@artigo@Índice Único vs Índice Composto no MongoDB](https://medium.com/@rakeebnazar/single-vs-compound-mongodb-index-in-depth-analysis-5319cfdd2ce)
