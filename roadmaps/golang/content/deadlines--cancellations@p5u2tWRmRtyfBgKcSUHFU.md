# Deadlines & Cancellações

Mecanismos do pacote Context para controlar a vida útil da operação e propagar sinalizadores de cancelamento. Suporta prazos (tempo absoluto) ou timeouts (duração). As funções devem verificar `ctx.Done()` e retornar cedo quando canceladas. Essencial para aplicativos concorrentes robustos.

Acesse os seguintes recursos para saber mais:

- [@oficial@Cancelando Operações em Progresso](https://go.dev/doc/database/cancel-operations)
- [@artigo@Compreendendo o Contexto do Go: Cancelamento, Timeouts](https://webdevstation.com/posts/understanding-golang-context/)
- [@artigo@Compreendendo Contexto no Go](https://medium.com/better-programming/understanding-context-in-golang-7f574d9d94e0)
- [@artigo@Como usar o método context.Done() em Go](https://dev.to/mcaci/how-to-use-the-context-done-method-in-go-22me)
