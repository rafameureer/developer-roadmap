# Buffer Overflow

Um buffer overflow ocorre quando um programa escreve mais dados em um buffer de tamanho fixo, como um array, do que ele pode conter, sobrescrevendo a memória adjacente. Isso pode corromper outras variáveis, fazer o programa crashar ou, em casos mais graves, ser explorado para executar código malicioso, tornando-se uma vulnerabilidade de segurança conhecida. Usar alternativas mais seguras às funções como `strcpy`, como `strncpy` ou `snprintf` com limites de tamanho explícitos, ajuda a prevenir isso.

Acesse os seguintes recursos para saber mais:

- [@artigo@Exploit de Buffer Overflow em C. Um breve resumo com um laboratório prático.](https://medium.com/@brendamejia/buffer-overflow-exploit-in-c-a-brief-overview-with-a-hands-on-lab-60e53d0d8d08)
- [@vídeo@Buffer Overflow em C, Corrupção de Heap/Stack e Análise](https://www.youtube.com/watch?v=CQ6pGrXY1Us)
- [@vídeo@Executando um Ataque de Buffer Overflow](https://www.youtube.com/watch?v=1S0aBV-Waeo)
