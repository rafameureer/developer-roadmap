# assert.h

O `<assert.h>` fornece a macro `assert`, que verifica se uma condição dada é verdadeira e, caso contrário, imprime uma mensagem de erro com o nome do arquivo e o número da linha antes de encerrar o programa. É comumente usado durante o desenvolvimento para capturar erros de programação cedo, como argumentos de função inválidos, em vez de deixá-los causar falhas mais difíceis de diagnosticar mais tarde. Definir a macro `NDEBUG` antes de incluir `<assert.h>` desativa todas as asserções, o que é geralmente feito em builds de versão para melhor desempenho.

Acesse os seguintes recursos para saber mais:

- [@article@Biblioteca C - \<assert.h\>](https://www.tutorialspoint.com/c_standard_library/assert_h.htm)
- [@article@Como usar asserções em C](https://ptolemy.berkeley.edu/~johnr/tutorials/assertions.html)
- [@video@Encontre bugs mais rápido usando asserções.](https://www.youtube.com/watch?v=1Jh9BUxIw0U)
