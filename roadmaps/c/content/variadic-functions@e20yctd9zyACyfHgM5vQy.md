# Funções Variádicas

Funções variádicas aceitam um número variável de argumentos, como `printf`, que pode receber qualquer número de valores dependendo da sua string de formato. Elas são declaradas usando um elipsis (`...`) como o último parâmetro e acessadas dentro da função usando macros do `<stdarg.h>`, como `va_start`, `va_arg` e `va_end`. Como o compilador não pode verificar os tipos dos argumentos variádicos da mesma forma que faz com os parâmetros regulares, desencaixes entre os tipos de argumento esperados e reais são uma fonte comum de bugs.

Acesse os seguintes recursos para saber mais:

- [@artigo@Funções Variádicas em C](https://www.tutorialspoint.com/cprogramming/c_variadic_functions.htm)
- [@vídeo@Como criar funções com um número variável de argumentos](https://www.youtube.com/watch?v=3iX9a_l9W9Y)
