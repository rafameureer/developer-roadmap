# Cursor

Os cursor no MongoDB são ponteiros para conjuntos de resultados de consultas que permitem a iteração eficiente em grandes conjuntos de dados sem carregar todos os documentos na memória. Eles suportam métodos como `hasNext(), next(), forEach()` e `limit()` para manipulação dos resultados. Os cursor lidam automaticamente com o batch, fornecem carregamento lento dos resultados e podem ser configurados com timeouts e tamanhos de batch para a performance ótima.

Acesse os seguintes recursos para saber mais:

- [@oficial@Cursor](https://www.mongodb.com/docs/manual/reference/method/js-cursor/)
- [@artigo@Entendendo Cursor no MongoDB](https://medium.com/@satyamguptaece/understanding-cursor-in-mongodb-b8a9e1a8cb0c)
