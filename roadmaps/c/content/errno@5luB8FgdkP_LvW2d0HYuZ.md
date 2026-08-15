# errno

`errno` é uma variável global, declarada em `<errno.h>`, que muitas funções da biblioteca padrão definem para um código de erro específico quando elas falham. Ele não é automaticamente resetado para zero em sucesso, então deve ser verificado apenas imediatamente após uma chamada de função documentada como definir, e geralmente depois de confirmar que a função realmente falhou. Funções como `perror` ou `strerror` traduzem um valor `errno` em uma mensagem legível para humanos.

Acesse os seguintes recursos para saber mais:

- [@artigo@Errno e Gerenciamento de Erros em C](https://www.codequoi.com/en/errno-and-error-management-in-c/)
- [@artigo@Guia para o Tratamento de Erros em C](https://psychocod3r.wordpress.com/2019/04/02/a-guide-to-error-handling-in-c/)
- [@vídeo@Tratando Erros em C/Unix (perror, strerror, errno)](https://www.youtube.com/watch?v=IZiUT-ipnj0)
