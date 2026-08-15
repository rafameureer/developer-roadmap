# O Problema do N+1 (N+1 Query Problem)

O problema do N+1 ocorre quando uma aplicação faz uma consulta inicial para buscar uma lista de registros (1 query) e, em seguida, executa uma consulta adicional separada no banco de dados para cada um dos registros retornados (N queries) para obter dados relacionados. Isso resulta em dezenas ou centenas de requisições desnecessárias ao banco, degradando severamente a performance. Esse problema é corrigido com técnicas de *Eager Loading*, junções otimizadas (*JOINs*) ou consultas em lote (*batching*).

Visite os seguintes recursos para aprender mais:

- [@article@Explicação Detalhada do Problema de Consulta N+1](https://medium.com/doctolib/understanding-and-fixing-n-1-query-30623109fe89)
- [@article@O que é o Problema do N+1 e Como Resolvê-lo](https://planetscale.com/blog/what-is-n-1-query-problem-and-how-to-solve-it)
- [@article@Resolvendo o Problema do N+1 em Aplicações Backend Java](https://dev.to/jackynote/solving-the-notorious-n1-problem-optimizing-database-queries-for-java-backend-developers-2o0p)
- [@video@SQLite e o Problema do N+1](https://www.youtube.com/watch?v=qPfAQY_RahA)
