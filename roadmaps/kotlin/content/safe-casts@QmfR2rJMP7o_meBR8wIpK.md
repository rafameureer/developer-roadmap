# Convesões Seguras

As conversões seguras em Kotlin fornecem uma maneira de converter uma variável de um tipo para outro, mas, ao contrário das conversões regulares, elas lidam com a possibilidade da conversão falhar de forma graciosamente. Em vez de lançar uma `ClassCastException` se a conversão não for possível, uma conversão segura retorna `null`. Isso permite que você tente de maneira segura uma conversão de tipo e trate o caso em que o objeto não é do tipo esperado sem quebrar seu programa.

Acesse os seguintes recursos para saber mais:

- [@oficial@Conversões Seguras](https://kotlinlang.org/docs/null-safety.html#safe-casts)
- [@vídeo@Conversão de Tipos Segura em Kotlin com 'as?'](https://www.youtube.com/watch?v=3ZvJb_f9jrU)
