# Threads POSIX

Threads POSIX, comumente chamadas de pthreads, é uma API padrão definida em `<pthread.h>` para criar e gerenciar threads em sistemas Unix-like, permitindo que um único processo execute várias sequências de instruções simultaneamente. Threads criadas desta forma compartilham o mesmo espaço de memória, o que habilita a comunicação rápida entre elas, mas também introduz o risco de condições de corrida quando múltiplas threads acessam os mesmos dados sem coordenação. Funções como `pthread_create` e `pthread_join` lidam com a criação de novas threads e espera por elas terminarem.

Acesse os seguintes recursos para saber mais:

- [@artigo@Bibliotecas POSIX thread (pthread)](https://www.cs.cmu.edu/afs/cs/academic/class/15492-f07/www/pthreads.html)
- [@artigo@Threads POSIX (pthreads) — A maneira mais simples de entender a multitarefa real em C](https://medium.com/@techdhaba.training/posix-threads-pthreads-the-simplest-way-to-understand-real-multithreading-in-c-c2f591ab7a03)
- [@vídeo@Como criar e unir threads em C (pthreads).](https://www.youtube.com/watch?v=uA8X5zNOGw8)
