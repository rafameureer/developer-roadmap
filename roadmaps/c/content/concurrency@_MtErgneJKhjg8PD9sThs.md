# Concorrência

A concorrência em C abrange a execução de várias sequências de execução, como threads ou processos, simultaneamente ou em uma intercalação. Isso inclui o uso de POSIX threads para paralelismo com memória compartilhada dentro de um único processo, mutexes para prevenir múltiplas threads de corromper dados compartilhados e comunicação entre processos para processos separados que precisam trocar dados. Escrever código C concorrente correto requer atenção cuidadosa ao estado compartilhado, já que o idioma não oferece proteção automática contra corridas de dados.

Acesse os seguintes recursos para saber mais:

- [@livro@Introdução à Programação Concorrente em C](https://storm-lang.org/progvis-book/book.pdf)
- [@artigo@Threads, Mutexes e Programação Concorrente em C](https://www.codequoi.com/en/threads-mutexes-and-concurrent-programming-in-c/)
- [@artigo@Concorrência em C](https://www.classes.cs.uchicago.edu/archive/2017/spring/12300-1/lab5.html)
- [@vídeo@Introdução a Threads (pthreads) | Tutorial de Programação em C](https://www.youtube.com/watch?v=ldJ8WGZVXZk)
