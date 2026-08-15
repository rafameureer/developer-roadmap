# Memoização em Fetch

Memoização é uma técnica de otimização que acelera chamadas subsequentes de função armazenando os resultados das chamadas anteriores com os mesmos parâmetros de entrada. Esse abordagem permite o reuso de dados em uma árvore de componentes React, previne chamadas de rede redundantes e melhora o desempenho.
Para a primeira solicitação, os dados são recuperados de uma fonte externa e o resultado é armazenado na memória
Solicitações subsequentes para os mesmos dados dentro da mesma passagem de renderização recuperam o resultado da memória, evitando a necessidade de fazer a solicitação novamente.

Acesse os seguintes recursos para saber mais:

- [@oficial@Memoização de Solicitação](https://nextjs.org/docs/app/guides/caching#request-memoization)
- [@vídeo@Tutorial do Next.js 14 - vRequest Memoization](https://www.youtube.com/watch?v=tcLe3Xi0fJE)
