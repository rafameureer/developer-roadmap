# $text

O operador `$text` no MongoDB realiza uma busca de texto completa em campos com índices de texto. Ele suporta correspondência de frases, stemming, palavras-chave e pontuação relevante. O `$text` pesquisa simultaneamente em todos os campos indexados por texto e fornece classificação baseada em pontuações dos resultados. Esse operador requer um índice de texto na coleção e habilita a funcionalidade de busca eficiente para aplicativos pesados em texto.

Acesse os seguintes recursos para saber mais:

- [@oficial@$text](https://www.mongodb.com/docs/manual/reference/operator/query/text/)
- [@artigo@Busca de Texto no MongoDB](https://devforid.medium.com/full-text-search-in-mongodb-655169b59fce)
