# WaitGroups

Primitiva de sincronização do pacote sync para esperar múltiplas goroutines terminarem. Use `Add()` para incrementar o contador, `Done()` quando a goroutine termina, e `Wait()` para bloquear até que o contador atinja zero. Essencial para coordenar a conclusão das goroutines em programas concorrentes.

Acesse os seguintes recursos para saber mais:

- [@artigo@WaitGroup em Go - Como e quando usar WaitGroup](https://medium.com/@dmytro.misik/waitgroup-in-go-df8f068e646f)
- [@artigo@Dominando a Concorrência em Golang](https://thelinuxcode.com/mastering-concurrency-in-golang-a-deep-dive-into-the-waitgroup/)
