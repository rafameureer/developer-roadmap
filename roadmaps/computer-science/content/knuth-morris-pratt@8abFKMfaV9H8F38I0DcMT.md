# Algoritmo Knuth Morris Pratt

O algoritmo Knuth Morris Pratt é um algoritmo de busca de strings que usa um array pré-computado para encontrar uma substring em uma string. Esse array é conhecido como a função prefixo. A função prefixo é o maior prefixo que também é sufixo de uma substring. A função prefixo é usada para pular os caracteres já correspondentes. O algoritmo segue os seguintes passos:

*   Computar a função prefixo da substring.
*   Navegar simultaneamente pela string e pela substring.
*   Se os caracteres forem correspondentes, incremente o índice tanto da string quanto da substring.
*   Se os caracteres não forem correspondentes, incremente o índice da string pelo valor da função prefixo no índice da substring.

Acesse os seguintes recursos para saber mais:

- [@curso@Algoritmo Knuth-Morris Pratt](https://www.coursera.org/learn/algorithms-part2/lecture/TAtDr/knuth-morris-pratt)
- [@vídeo@9.1 Algoritmo Knuth-Morris-Pratt KMP String Matching Algorithm](https://www.youtube.com/watch?v=V5-7GzOfADQ)
