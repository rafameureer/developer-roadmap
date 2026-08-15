# var vs :=

O Go fornece duas maneiras principais de declarar variáveis: usando `var` e usando o operador de declaração curta `:=`.

A palavra-chave `var` é usada para declarações explícitas de variáveis. Você pode usá-la para definir uma variável com ou sem atribuir um valor. Se nenhum valor for fornecido, Go atribui um valor padrão _zero value_ baseado no tipo da variável. `var` pode ser usado tanto dentro quanto fora das funções.

A sintaxe `:=` é um atalho para declarar e inicializar uma variável. Ele infere o tipo a partir do valor e só pode ser usado **dentro de funções**. É uma maneira rápida e conveniente de criar variáveis sem mencionar explicitamente seus tipos.

Visite os seguintes recursos para aprender mais:

- [@official@Tour Go: Declaração de Variável Curta](https://go.dev/tour/basics/10)
- [@official@Especificação Go: Declaração de Variável Curta](https://go.dev/ref/spec#Short_variable_declarations)
