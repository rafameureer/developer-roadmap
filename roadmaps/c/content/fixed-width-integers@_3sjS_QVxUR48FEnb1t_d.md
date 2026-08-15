# Inteiros de largura fixa

Os tipos de inteiros de largura fixa, definidos em `<stdint.h>`, como `int32_t` ou `uint8_t`, garantem uma largura exata de bits independentemente da plataforma, ao contrário dos tipos `int` ou `long`, cujos tamanhos podem variar. Isso os torna úteis para escrever código portável, especialmente em redes, formatos de arquivo e sistemas embarcados onde tamanhos exatos importam. Usá-los evita bugs sutis que surgem da suposição de um tamanho de tipo sem verificar.

Acesse os seguintes recursos para saber mais:

- [@artigo@Inteiros de largura fixa](https://www.w3schools.com/c/c_fixed_width_ints.php)
- [@artigo@Tipos de inteiros de largura fixa (desde C99)](https://en.cppreference.com/c/types/integer)
