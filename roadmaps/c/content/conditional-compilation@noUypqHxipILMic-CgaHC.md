# Compilação Condicional

A compilação condicional usa diretivas de pré-processador como `#ifdef`, `#ifndef`, `#if` e `#endif` para incluir ou excluir blocos de código antes que o compilador os processe, com base em whether certas macros estão definidas. É comumente usado para código específico da plataforma, permitindo seções de depuração exclusivas ou impedindo que um arquivo de cabeçalho seja incluído múltiplas vezes através dos guardas de cabeçalho. Porque isso acontece durante o pré-processamento, o código excluído nunca é visto pelo compilador.

Acesse os seguintes recursos para saber mais:

- [@artigo@Diretivas de compilação condicional em C](https://fastbitlab.com/blog/microcontroller-embedded-c-programming-lecture-182-conditional-compilation-directives/)
- [@artigo@Compilação condicional - Wikipedia](https://en.wikipedia.org/wiki/Conditional_compilation)
- [@vídeo@Diretivas de compilação condicional](https://www.youtube.com/watch?v=rTNDAMyRpUs)
