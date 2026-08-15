# Perda de Memória

Uma perda de memória ocorre quando a memória dinamicamente alocada não é mais necessária, mas nunca é liberada, então ela permanece reservada e indisponível para o resto da execução do programa. As perdas acumulam ao longo do tempo, especialmente em programas que duram por muito tempo, e podem eventualmente esgotar toda a memória disponível. Ferramentas como Valgrind podem detectar as perdas rastreando alocações que nunca são correspondidas com um `free` adequado.

Acesse os seguintes recursos para saber mais:

- [@artigo@Como encontrar uma perda de memória em C ou C++](https://www.parasoft.com/blog/finding-memory-leaks-in-c-or-c/)
- [@artigo@Como encontrar e corrigir perdas de memória em C ou C++](https://www.netdata.cloud/academy/how-to-find-memory-leak-in-c/)
- [@vídeo@Perdas de Memória e Como Prevenir Elas](https://www.youtube.com/watch?v=lQCLAKfcYI4)
