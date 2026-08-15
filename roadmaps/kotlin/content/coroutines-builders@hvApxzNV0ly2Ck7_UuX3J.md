# Construtores de Corrotina

Construtores de corrotina em Kotlin são funções que iniciam uma nova corrotina. Eles servem como ponte entre o código regular, bloqueante e o mundo não-bloqueante e concorrente das corrotinas. Construtores comuns incluem `launch`, que inicia uma corrotina sem bloquear a thread atual e retorna um `Job`, e `runBlocking`, que bloqueia a thread atual até a corrotina terminar, principalmente usada para testes e funções principais. Outro construtor, `async`, inicia uma corrotina e retorna um objeto `Deferred`, que representa um resultado futuro. Esses construtores permitem executar código de forma concorrente e gerenciar o ciclo de vida das corrotinas.

Acesse os seguintes recursos para saber mais:

- [@oficial@Básicos de Corrotina](https://kotlinlang.org/docs/coroutines-basics.html#your-first-coroutine)
- [@artigo@Construtores de Corrotina em Kotlin](https://medium.com/@appdevinsights/kotlin-coroutine-builders-6a6639cc478d)
