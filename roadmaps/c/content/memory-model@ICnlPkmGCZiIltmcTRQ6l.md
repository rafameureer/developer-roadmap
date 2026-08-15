# Modelo de Memória

O modelo de memória em C descreve como a memória de um programa em execução é organizada em regiões distintas: a pilha para variáveis locais e informações de chamadas de função, o heap para memória dinamicamente alocada, e segmentos separados para variáveis globais/estáticas e o próprio código do programa compilado. Entender essa disposição ajuda a explicar por que algumas memórias são automaticamente recuperadas e outras memórias devem ser liberadas manualmente. Também esclarece por que certos bugs, como estouro de pilha ou corrupção de heap, ocorrem em regiões específicas.

Acesse os seguintes recursos para saber mais:

- [@artigo@Modelo de Memória](https://en.cppreference.com/c/language/memory_model#:~:text=Defines%20the%20semantics%20of%20computer,memory%20has%20a%20unique%20address.)
- [@artigo@O Modelo de Memória em C](https://www.cs.toronto.edu/~strider//docs/ICS_Chapter_2.pdf)
- [@vídeo@Programação em C e Gerenciamento de Memória - Curso Completo](https://www.youtube.com/watch?v=rJrd2QMVbGM)
