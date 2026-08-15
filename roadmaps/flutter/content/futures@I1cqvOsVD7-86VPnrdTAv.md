# Futuras

As futuras em Flutter são uma maneira de representar um valor potencial que estará disponível em algum momento no futuro. Alguns pontos importantes sobre as futuras em Flutter:

*   As futuras são usadas para programação assíncrona em Flutter
*   As futuras retornam um único valor (ou um erro) e geralmente são usadas com `async` e `await`.
*   O método `then` pode ser usado para anexar uma callback a uma futura que será executada assim que o valor da futura estiver disponível.
*   Futuras podem ser combinadas com outras futuras usando os métodos `Future.wait` ou `Future.whenComplete`.
*   As futuras são frequentemente usadas com solicitações de rede, operações de E/S de arquivo e outras tarefas de longo prazo em Flutter.

Acesse os seguintes recursos para saber mais:

- [@oficial@Futuras e Tratamento de Erros](https://dart.dev/guides/libraries/futures-error-handling)
