# Níveis de otimização

Níveis de otimização, definidos com sinalizadores do compilador como `-O0` até `-O3` no GCC e Clang, controlam o quão agressivamente o compilador transforma o código para melhorar o desempenho, às vezes à custa de tempos de compilação mais longos e comportamento de depuração menos previsível. `-O0` desativa completamente a otimização, o que é útil durante o desenvolvimento porque o código compilado se aproxima muito do código-fonte. Níveis mais altos podem reordenar, embutir ou eliminar código de maneiras que tornem a depuração passo a passo mais difícil de seguir e também podem expor comportamentos indefinidos que pareciam funcionar corretamente em níveis de otimização mais baixos.

Acesse os seguintes recursos para saber mais:

- [@artigo@Otimização de Programas em C](https://icps.u-strasbg.fr/~bastoul/local_copies/lee.html)
- [@artigo@Compilador otimizador](https://en.wikipedia.org/wiki/Optimizing_compiler)
- [@vídeo@Fundamentos da otimização do compilador em C](https://www.youtube.com/watch?v=-gZpBCRaEak)
