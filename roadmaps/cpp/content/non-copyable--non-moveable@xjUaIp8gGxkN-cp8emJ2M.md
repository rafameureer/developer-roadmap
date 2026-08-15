# Non-Copiável / Não-Movível

O idiom non-copiável/non-movível em C++ impede que objetos de uma classe sejam copiados ou movidos. Isso é feito excluindo o construtor de cópia, o operador de atribuição de cópia, o construtor de movimento e o operador de atribuição de movimento. É útil para classes que gerenciam recursos exclusivos, garantindo que apenas uma instância controle o recurso em um determinado momento, previnindo problemas como duplicação de recursos ou deleção dupla. Ao desabilitar a cópia e o movimento, você impõe um modelo de propriedade única para as instâncias da classe.

Acesse os seguintes recursos para saber mais:

- [@artigo@Lidando com objetos não-copiáveis - (Tutorial em C++)](https://dev.to/dabretema/the-day-i-forbade-copy-semantics-to-an-object-nkl)
