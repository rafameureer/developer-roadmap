# Strings

O C representa strings como arrays de `char` terminados por um caractere nulo (`\0`), em vez de como um tipo de string distinto. Devido a isso, o tratamento de strings depende da conhecimento exato da localização do caractere nulo terminal, e funções como `strlen`, `strcpy` e `strcmp` da biblioteca `<string.h>` operam nesta convenção. Esquecer de contar o byte extra do caractere nulo terminal ou copiar uma string em um buffer que não é grande o suficiente para abri-la são fontes frequentes de bugs.

Acesse os seguintes recursos para saber mais:

- [@article@C Strings](https://www.w3schools.com/c/c_strings.php)
- [@article@C/Strings](https://www.cs.yale.edu/homes/aspnes/pinewiki/C(2f)Strings.html)
- [@video@Básico de String | Tutorial de Programação em C](https://www.youtube.com/watch?v=60OI5tzmkCw)
- [@video@String em Array de Caracteres VS. Ponteiro para Literal de String](https://www.youtube.com/watch?v=Qp3WatLL_Hc)
