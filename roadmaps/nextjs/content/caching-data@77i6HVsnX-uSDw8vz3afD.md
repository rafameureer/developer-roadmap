# Cacheamento de Dados

O cacheamento de dados no Next.js envolve armazenar os resultados das chamadas de dados para que solicitações subsequentes para os mesmos dados possam ser servidas mais rapidamente. Em vez de repetir a obtenção de dados de um banco de dados ou API, o Next.js pode recuperá-los do cache. Isso melhora o desempenho e reduz a carga em suas fontes de dados. O cacheamento pode ser configurado em diferentes níveis.

O comportamento de cacheamento muda dependendo se a rota é renderizada estáticamente ou dinamicamente, se os dados são armazenados em cache ou não, e se uma solicitação faz parte de uma visita inicial ou uma navegação subsequente. Dependendo do seu caso de uso, você pode configurar o comportamento de cacheamento para rotas individuais e solicitações de dados.

Acesse os seguintes recursos para saber mais:

- [@oficial@Cacheamento e Revalidação](https://nextjs.org/docs/app/getting-started/caching-and-revalidating)
