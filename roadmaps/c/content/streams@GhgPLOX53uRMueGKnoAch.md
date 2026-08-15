# Streams

Um stream em C é uma abstração que representa uma fonte ou destino de dados, como um arquivo, o teclado ou a tela, acessados através de um ponteiro `FILE *`. A biblioteca padrão fornece três streams automaticamente: `stdin` para entrada, `stdout` para saída normal e `stderr` para saída de erros. Funções como `fopen`, `fread`, `fwrite` e `fclose` operam em streams em vez de diretamente no descritor de arquivo subjacente.

Acesse os seguintes recursos para saber mais:

- [@article@C programming/Stream IO](https://en.wikibooks.org/wiki/C_programming/Stream_IO)
