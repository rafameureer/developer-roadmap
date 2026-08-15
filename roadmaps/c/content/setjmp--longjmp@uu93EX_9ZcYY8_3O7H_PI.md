# setjmp / longjmp

`setjmp` e `longjmp`, declarados em `<setjmp.h>`, implementam um salto não-local que permite a um programa salvar um ponto de execução com `setjmp` e depois voltar para ele com `longjmp`, potencialmente desfazendo várias chamadas de função de uma só vez. Isso às vezes é usado como uma substituição rústica para o tratamento de exceções, por exemplo, para recuperar-se de um erro profundo em uma pilha de chamadas. Porque ele pula a limpeza normal das funções, como chamar destrutores em C++, deve ser usado com cuidado e não existe para tornar o tratamento de erros elegante, apenas possível.

Acesse os seguintes recursos para saber mais:

- [@artigo@setjmp(), longjmp() e Tratamento de Exceções em C](https://dev.to/pauljlucas/setjmp-longjmp-and-exception-handling-in-c-1h7h)
- [@vídeo@Posso Lidar com Exceções com Try Catch em C? (setjmp, longjmp)](https://www.youtube.com/watch?v=eQcRcgOnl9o)
