# Em funções de seta

As funções de seta não têm seu próprio vinculamento `this`. Em vez disso, elas herdam `this` do escopo léxico onde foram definidas. Isso torna as funções de seta previsíveis em callbacks e manipuladores de eventos onde as funções regulares perderiam o contexto `this` intencional.

Acesse os seguintes recursos para saber mais:

- [@artigo@Palavra-chave this e função de seta](https://stackoverflow.com/questions/66518020/javascript-this-keyword-and-arrow-function)
