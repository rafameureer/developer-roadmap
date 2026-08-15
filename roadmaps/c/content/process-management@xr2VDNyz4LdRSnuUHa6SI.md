# Gerenciamento de Processos

O gerenciamento de processos abrange a criação, controle e terminação de processos dentro de um programa em C, geralmente usando funções POSIX como `fork` para criar um novo processo, `exec` para substituir o programa de um processo por um novo e `wait` para que um processo pai espere até que um filho termine. Isso é a base do funcionamento de shells e outros programas ao iniciar e gerenciar outros programas. Ele está estreitamente relacionado, mas distinto da concorrência, pois processos separados têm seu próprio espaço de memória independente, em vez de threads.

Acesse os seguintes recursos para saber mais:

- [@artigo@Gerenciamento de Processos: Sistema Operacional](https://dev.to/harshm03/process-management-operating-system-18gl)
- [@artigo@Dominando fork() e exec() em C: A Guia Completa do Iniciante para o Gerenciamento de Processos em Sistemas Unix-like](https://levelup.gitconnected.com/mastering-fork-and-exec-in-c-a-beginners-guide-to-process-management-in-unix-like-operating-81b2b19b4dfe)
- [@vídeo@Gerenciamento de Processos (Processos e Threads)](https://www.youtube.com/watch?v=OrM7nZcxXZU)
