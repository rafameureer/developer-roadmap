# Idioma Comma-Ok

Padrão para testar a existência de uma chave em um mapa ou a sucesso de uma declaração de tipo usando `value, ok := map[key]` ou `value, ok := interface.(Type)`. Retorna tanto o valor quanto o status booleano, evitando panics e distinguindo valores zero de chaves ausentes.

Acesse os seguintes recursos para saber mais:

- [@artigo@O Idioma Comma Ok](https://dev.to/saurabh975/comma-ok-in-go-l4f)
- [@artigo@Como o Idioma Comma Ok e o Sistema de Pacotes Funcionam em Go](https://www.freecodecamp.org/news/how-the-comma-ok-idiom-and-package-system-work-in-go/)
- [@artigo@Idiomas de Declaração em Go](https://medium.com/@nateogbonna/statement-idioms-in-go-writing-clean-idiomatic-go-code-6fe92e6e8ab4)
