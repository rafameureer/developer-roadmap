# Modo Binário vs Modo Texto

O modo texto pode traduzir certos caracteres, especialmente as terminações de linha, ao ler ou escrever um arquivo, convertendo entre a convenção de terminação de linha nativa do sistema operacional e uma representação interna consistente. O modo binário não realiza tal tradução, transferindo bytes exatamente como estão armazenados. Em sistemas Unix-like, os dois modos se comportam da mesma forma, mas no Windows a distinção importa, pois o modo texto traduz entre `\n` e `\r\n`.

Acesse os seguintes recursos para saber mais:

- [@article@Manipulação de Arquivos em C](https://www.programiz.com/c-programming/c-file-input-output)
- [@video@Introdução ao Acesso a Arquivos Binários | Exemplo de Programação em C](https://www.youtube.com/watch?v=UtckqNKZFrA)
