# Interfaces de Sistema Operacional e Sinais

As interfaces de sistema operacional e sinais, como `<signal.h>` e partes de `<stdlib.h>`, permitem que um programa em C interaja com o sistema operacional subjacente, incluindo o tratamento de eventos assíncronos como interrupções (`SIGINT`) ou a configuração de respostas personalizadas para sinais gerados pelo sistema. Essas funções fornecem uma maneira portátil, se limitada, de escrever programas que respondam a eventos externos como um usuário pressionando Ctrl+C. Uma interação mais extensa com o sistema operacional, como a criação de processos, geralmente requer APIs específicas da plataforma, como funções POSIX em sistemas Unix-like.

Acesse os seguintes recursos para saber mais:

- [@artigo@Biblioteca C - \<signal.h\>](https://www.tutorialspoint.com/c_standard_library/signal_h.htm)
