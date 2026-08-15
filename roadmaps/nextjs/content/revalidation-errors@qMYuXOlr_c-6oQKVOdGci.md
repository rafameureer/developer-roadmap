# Erros de Revalidação

Quando a revalidação falha, significa que o tentativa de atualizar os dados em cache encontrou um problema, impedindo que a aplicação exiba as informações mais recentes. Esses erros podem surgir de várias fontes, como problemas de conectividade de rede, problemas com a própria fonte de dados (por exemplo, um banco de dados indisponível) ou problemas na lógica de revalidação. Na Next.js, se ocorrer um erro ao tentar revalidar os dados, os últimos dados gerados com sucesso continuarão sendo servidos do cache. Na próxima solicitação subsequente, a Next.js tentará revalidar os dados novamente.

Acesse os seguintes recursos para saber mais:

- [@oficial@Tratamento de erros e revalidação](https://nextjs.org/docs/14/app/building-your-application/data-fetching/fetching-caching-and-revalidating)
