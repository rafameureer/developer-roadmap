# Qualificador restrict

O qualificador `restrict`, introduzido em C99, é uma dica para o compilador que um ponteiro é a única maneira de acessar a memória à que ele aponta durante sua vida útil. Isso permite que o compilador faça otimizações mais agressivas, pois não precisa se proteger contra outro ponteiro aliasando a mesma memória. Usar incorretamente `restrict` ao realmente aliasar a memória resulta em comportamento indefinido.

Acesse os seguintes recursos para saber mais:

- [@artigo@Qualificador restrict](https://en.cppreference.com/c/language/restrict)
- [@vídeo@O único keyword do C sem equivalente no C++](https://www.youtube.com/watch?v=TBGu3NNpF1Q&t=58s)
