# Iteração em Strings

Itere sobre strings com `for range` para obter runes (pontos de código Unicode) e não bytes. Retorna o índice e o valor do rune. O acesso direto `str[i]` dá bytes. Use `[]rune(str)` para converter a string em um slice de runes para acesso aleatório. Importante para o tratamento de caracteres Unicode.

Acesse os seguintes recursos para saber mais:

- [@artigo@Iteradores em GoLang](https://blog.alexoglou.com/posts/iterators-golang/)
- [@artigo@Como iterar uma string em Go](https://labex.io/tutorials/go-how-to-iterate-string-in-go-446115)
- [@artigo@Dominando a Manipulação de Strings em Go: Funções e Exemplos Essenciais para 2024](https://learngolanguage.com/mastering-golang-string-manipulation-essential-functions-and-techniques-for-2024/)
