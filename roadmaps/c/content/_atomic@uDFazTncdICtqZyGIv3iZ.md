# _Atomic

O qualificador `_Atomic`, introduzido no C11, marca uma variável de forma que leituras e escritas nela ocorram como uma única operação indivisível, mesmo quando acessadas por múltiplas threads. Isso previne corridas de dados nesta variável sem a necessidade de um bloqueio separado. É usado em conjunto com o cabeçalho `<stdatomic.h>` ao escrever código C concorrente.

Acesse os seguintes recursos para saber mais:

- [@artigo@Tipos atômicos](https://en.cppreference.com/c/language/atomic)
- [@artigo@O que é a palavra-chave _Atomic em C?](https://www.educative.io/answers/what-is-the-atomic-keyword-in-c)
- [@artigo@Compreendendo Tipos Atômicos em C](https://andrewjohnson4.substack.com/p/understanding-_atomic-types-in-c)
