# Estados de Erro

Os estados de erro na roteirização do Next.js se referem a como sua aplicação lida com situações em que uma rota não pode ser carregada ou renderizada com sucesso. Os erros podem ser divididos em duas categorias: erros esperados e exceções não capturadas.

Erros esperados são aqueles que podem ocorrer durante o funcionamento normal da aplicação, como os de validação de formulários do lado do servidor ou solicitações falhas. Esses erros devem ser tratados explicitamente e retornados ao cliente.

Exceções não capturadas são erros inesperados que indicam bugs ou problemas que não devem ocorrer durante o fluxo normal da sua aplicação. Esses devem ser tratados lançando erros, que serão então capturados por limitações de erro.

Acesse os seguintes recursos para saber mais:

- [@oficial@Tratamento de Erros](https://nextjs.org/docs/app/getting-started/error-handling#handling-expected-errors)
- [@vídeo@Tutorial do Next.js 15 - Tratamento de Erros](https://www.youtube.com/watch?v=fWV5WPSbgdg)
