# Função React Cache

A função `cache` do React permite que você memoize o valor de retorno de uma função, permitindo que você chame a mesma função várias vezes enquanto ela é executada apenas uma vez.

Requisições `fetch` usando os métodos `GET` ou `HEAD` são automaticamente memoizadas, então você não precisa envolvê-las na função `cache` do React. No entanto, para outros métodos de `fetch`, ou quando usar bibliotecas de busca de dados (como alguns bancos de dados, CMS ou clientes GraphQL) que não memórias internamente as solicitações, você pode usar `cache` para memoizar manualmente as solicitações de dados.

Acesse os seguintes recursos para saber mais:

- [@oficial@Função React cache](https://nextjs.org/docs/app/guides/caching#react-cache-function)
