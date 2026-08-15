# Tipo de Dado Texto

O tipo de dado `text` no Elasticsearch é projetado para armazenar e indexar conteúdo de texto completo, como posts de blog, artigos ou descrições de produtos. Quando você indexa um campo como `text`, o Elasticsearch analisa o texto usando um analisador. Esse processo envolve quebrar o texto em termos individuais (tokens), colocá-los em minúsculas, remover palavras-chave e aplicar stemming. Essa análise permite ao Elasticsearch realizar buscas de texto completo, permitindo aos usuários encontrar documentos com base em palavras-chave ou frases relevantes no texto.

Acesse os seguintes recursos para saber mais:

- [@oficial@Família de tipos text](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/text-type-family)
- [@oficial@Análise de texto](https://www.elastic.co/docs/manage-data/data-store/text-analysis)
- [@artigo@Elasticsearch Keyword vs. Text](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-strings-keyword-vs-text-vs-wildcard/)
- [@artigo@Elasticsearch: Texto vs. Keyword](https://www.codecurated.com/blog/elasticsearch-text-vs-keyword/)
