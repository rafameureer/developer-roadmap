# Fluxo de Solicitação-Resposta

No Laravel, o fluxo de solicitação-resposta começa quando um usuário envia uma solicitação para a aplicação. Esta solicitação primeiro atinge o arquivo `public/index.php`, que inicializa o framework do Laravel. A solicitação é então passada para o kernel HTTP, que identifica a rota adequada com base na URI da solicitação. A rota em seguida chama uma ação de controlador ou fechamento, que processa a solicitação e gera uma resposta. Finalmente, a resposta é enviada de volta ao navegador do usuário.

Acesse os seguintes recursos para saber mais:

- [@oficial@Ciclo de Vida da Solicitação](https://laravel.com/docs/lifecycle)
- [@artigo@Entendendo o Ciclo de Vida da Solicitação/Resposta no Laravel: Um Guia Simples para Desenvolvedores](https://chandankshaw.medium.com/understanding-the-laravel-request-response-lifecycle-a-simple-guide-for-developers-e6afdf887a6d)
- [@artigo@Solicitações e Respostas](https://www.fastcomet.com/tutorials/laravel/requests-and-responses)
