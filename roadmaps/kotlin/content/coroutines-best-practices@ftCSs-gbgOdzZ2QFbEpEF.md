# Melhores Práticas de Coroutines

As coroutines em Kotlin simplificam o programação assíncrona, mas usar efetivamente elas requer seguir algumas melhores práticas. Isso inclui usar a concorrência estruturada para gerenciar os ciclos de vida das coroutines e prevenir vazamentos, evitando `GlobalScope` para a maioria das tarefas e preferindo `CoroutineScope` ligado a componentes específicos, lidando adequadamente com exceções dentro das coroutines e offloading operações longas ou bloqueantes para dispatchers apropriados como `Dispatchers.IO` para evitar bloquear a thread principal. Além disso, é importante cancelar as coroutines quando elas não forem mais necessárias para liberar recursos e prevenir trabalho desnecessário.

Visite os seguintes recursos para aprender mais:

- [@artigo@Melhores Práticas de Coroutine](https://medium.com/@vivekbansal19/coroutine-best-practices-affddb50ae1b)
- [@artigo@Melhores práticas para coroutines em Android](https://developer.android.com/kotlin/coroutines/coroutines-best-practices)
