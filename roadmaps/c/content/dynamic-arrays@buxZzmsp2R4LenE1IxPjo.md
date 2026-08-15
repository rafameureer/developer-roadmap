# Arrays Dinâmicos

Um array dinâmico é uma estrutura semelhante a um array que pode crescer ou diminuir em tempo de execução, geralmente implementada alocando memória na pilha e realocando um bloco maior, frequentemente usando `realloc`, quando não houver espaço suficiente. Diferentemente de um array de tamanho fixo do C, ele rastreia separadamente seu comprimento atual e sua capacidade alocada. Este padrão subjacente às tipos de arrays dinâmicos como o `std::vector` em C++ ou a lista em Python, embora o C exija implementá-lo manualmente.

Acesse os seguintes recursos para saber mais:

- [@artigo@Arrays Dinâmicos em C](https://www.bytesbeneath.com/p/dynamic-arrays-in-c?hide_intro_popup=true)
- [@artigo@Implementação de Arrays Dinâmicos em C: Um guia](https://medium.com/@sohaib.arshid101/dynamic-arrays-in-c-an-implementation-guide-4a959de94332)
- [@vídeo@Arrays Dinâmicos em C](https://www.youtube.com/watch?v=_KSKH8C9Gf0)
