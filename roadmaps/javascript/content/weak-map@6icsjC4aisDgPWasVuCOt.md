# Weak Map

A `WeakMap` é uma coleção de pares chave-valor onde as chaves devem ser objetos e são mantidas com referências frágeis. Se o objeto-chave for coletado pelo garbage collector, a entrada será removida automaticamente da `WeakMap`. Ela é usada para armazenar dados privados associados a objetos sem prevenir a coleta de lixo.

Acesse os seguintes recursos para saber mais:

- [@artigo@WeakMap](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
- [@artigo@WeakMap e WeakSet](https://javascript.info/weakmap-weakset)
