# Mutexes

Barramentos de exclusão mútua do pacote sync garantindo que apenas uma goroutine acesse um recurso compartilhado por vez. Use `Lock()` antes e `Unlock()` após a seção crítica. RWMutex permite múltiplos leitores ou um único escritor. Essencial para proteger dados compartilhados de condições de corrida.

Acesse os seguintes recursos para saber mais:

- [@artigo@O que é Mutex e como usá-lo em Go?](https://dev.to/lincemathew/what-is-mutex-and-how-to-use-it-in-golang-1m1i)
- [@artigo@Entendendo Mutex em Go Introdução](https://kamnagarg-10157.medium.com/understanding-mutex-in-go-5f41199085b9)
