# ASan & LSan

AddressSanitizer (ASan) e LeakSanitizer (LSan) são ferramentas integradas ao compilador, ativadas com uma bandeira como `-fsanitize=address`, que detectam erros de memória e vazamentos, respectivamente, instrumentando o código compilado para verificar acessos à memória em tempo de execução. ASan captura problemas como estouro de buffer, uso após a liberação e uso de memória após ela sair do escopo, relatando a localização exata do erro. Em comparação com ferramentas como Valgrind, os sanitizadores geralmente são mais rápidos porque as verificações estão incorporadas no próprio binário compilado em vez de serem emuladas externamente.

Acesse os seguintes recursos para saber mais:

- [@artigo@AddressSanitizer](https://learn.microsoft.com/en-gb/cpp/sanitizers/asan?view=msvc-170)
- [@vídeo@Encontre erros de memória rapidamente. (-fsanitize, addresssanitizer)](https://www.youtube.com/watch?v=tEbV21aPSKw)
- [@vídeo@Detecte vazamentos de memória em C++ com ALSan:](https://www.youtube.com/watch?v=9f5hd-8suVE)
