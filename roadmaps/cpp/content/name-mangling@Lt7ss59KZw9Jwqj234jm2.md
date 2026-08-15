# Mangling de Nomes

O mangling de nomes, também conhecido como decoração de nome, é uma técnica usada pelos compiladores para codificar informações extras como escopo, tipo e vinculação em nomes de identificadores (como nomes de funções e variáveis). Isso permite que o C++ suporte sobrecarga de função, onde várias funções podem compartilhar o mesmo nome mas terem parâmetros diferentes. O compilador gera um nome mangulado com base nessas detalhes, embora as regras exatas de mangling varie entre compiladores e plataformas. Ferramentas como `c++filt` podem desmangar esses nomes de volta para sua forma original, o que é útil para depuração. Embora você geralmente não precise entender os detalhes do mangling de nomes, ele pode ser importante quando trabalhar com bibliotecas externas ou vincular arquivos objeto de diferentes compiladores.

Acesse os seguintes recursos para saber mais:

- [@artigo@Mangling de Nomes em C++](https://medium.com/@abhishek.ec/c-name-mangling-ce3d0fedf88d)
- [@vídeo@Mangling de Nomes em C++](https://www.youtube.com/watch?v=FUIle4Ghasw)
