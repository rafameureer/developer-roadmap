# Unions

Um `union` permite que vários membros compartilhem a mesma localização de memória, então apenas um membro possui um valor válido em qualquer momento dado, e o tamanho da union é igual ao do seu maior membro. Isso é útil para economizar memória quando diferentes pedaços de dados nunca são necessários simultaneamente ou para interpretar os mesmos bytes de maneiras diferentes. Ler um membro de uma union diferente do que foi escrito mais recentemente geralmente causa comportamento indefinido, exceto em casos específicos em que o padrão permite.

Acesse os seguintes recursos para saber mais:

- [@article@Unions em C](https://www.tutorialspoint.com/cprogramming/c_unions.htm)
- [@article@Declaração de Union](https://en.cppreference.com/c/language/union)
- [@video@Introdução a Unions em C](https://www.youtube.com/watch?v=oySsPUDr35U)
