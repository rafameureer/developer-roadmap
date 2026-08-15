# Buffers Círculares / Filas FIFO

Um buffer circular, ou buffer cíclico, é um buffer de tamanho fixo que se volta para o início uma vez chegar ao fim, tornando-se eficiente para implementar filas first-in-first-out sem deslocar elementos. Ele rastreia uma posição de leitura e uma posição de escrita que ambos se voltam pelo comprimento do buffer. Buffers cíclicos são comuns em sistemas embarcados e aplicações de streaming onde os dados chegam continuamente e a memória precisa permanecer limitada.

Acesse os seguintes recursos para saber mais:

- [@artigo@Criando um Buffer Circular em C e C++](https://embeddedartistry.com/blog/2017/05/17/creating-a-circular-buffer-in-c-and-c/)
- [@vídeo@Buffer Circular | Implementação de Buffer Circular em C](https://www.youtube.com/watch?v=uvD9_Wdtjtw)
