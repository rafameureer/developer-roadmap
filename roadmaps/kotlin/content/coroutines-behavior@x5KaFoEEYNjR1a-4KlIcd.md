# Comportamento de Coroutines

Iniciar uma coroutine a partir de um `CoroutineScope` cria um contexto que governa sua execução. Funções construtoras como `.launch()` e `.async()` criam automaticamente um conjunto de elementos que definem como a coroutine se comporta, incluindo a interface `Job`, que rastreia o ciclo de vida da coroutine e habilita a concorrência estruturada; `CoroutineDispatcher`, que controla onde a coroutine será executada; e `CoroutineExceptionHandler`, que lida com exceções não capturadas.

Visite os seguintes recursos para aprender mais:

- [@oficial@Conceitos de Coroutine](https://kotlinlang.org/docs/coroutines-basics.html)
- [@vídeo@Contextos de Coroutine - Kotlin Coroutines](https://www.youtube.com/watch?v=71NrkkRNXG4)
