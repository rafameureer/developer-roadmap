# Códigos de Saída

Um código de saída é um pequeno inteiro que um programa retorna para o sistema operacional quando termina, indicando se ele teve sucesso ou falhou, e se falhou, às vezes por quê. Por convenção, um código de saída de 0 significa sucesso e qualquer valor não nulo indica um erro, com `EXIT_SUCCESS` e `EXIT_FAILURE` da `<stdlib.h>` fornecendo constantes portáteis para esses. Os códigos de saída são comumente verificados por scripts shell e outros programas que chamam um programa C e precisam saber se ele foi concluído com sucesso.

Acesse os seguintes recursos para saber mais:

- [@artigo@Códigos de Saída em Programação Linux C](https://medium.com/@linuxrootroom/exit-codes-in-linux-c-programming-14dd90c4b48d)
- [@artigo@exit](https://en.cppreference.com/c/program/exit)
- [@vídeo@Obtendo o código de status de saída em C](https://www.youtube.com/watch?v=DiNmwwQWl0g)
