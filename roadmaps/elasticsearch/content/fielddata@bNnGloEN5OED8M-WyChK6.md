# Fielddata

Fielddata é uma estrutura de dados em disco usada pelo Elasticsearch para habilitar agregações, classificações e scripts em campos de texto. Como os campos de texto são analisados (quebrados em termos individuais), o Elasticsearch precisa de um modo de acessar rapidamente todos os termos para um documento específico durante essas operações. O Fielddata carrega todos os termos de um campo na memória, permitindo acesso rápido durante essas operações.

Acesse os seguintes recursos para saber mais:

- [@artigo@O que é o Fielddata do Elasticsearch?](https://pulse.support/kb/what-is-elasticsearch-fielddata)
- [@artigo@Fielddata do Elasticsearch](https://opster.com/guides/elasticsearch/glossary/elasticsearch-fielddata/)
- [@vídeo@Field Data vs Doc Values | Entendendo Problemas de Desempenho do Elasticsearch](https://www.youtube.com/watch?v=l99lIuvQULk)
