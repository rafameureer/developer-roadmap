# Regra de Zero, Cinco e Três

A Regra de Zero, Cinco e Três são diretrizes para gerenciar recursos dentro das classes e structs em C++. A Regra de Zero sugere deixar o compilador lidar com o gerenciamento de recursos se sua classe não explicitamente gerenciar nenhum. Se sua classe gerencia recursos, antes do C++11, ela seguiu a Regra de Três, exigindo que você defina um destrutor, construtor de cópia e operador de atribuição de cópia. O C++ moderno com semântica de movimento estende isso para a Regra de Cinco, que adiciona um construtor de movimento e um operador de atribuição de movimento para transferir eficientemente a propriedade dos recursos.

Acesse os seguintes recursos para saber mais:

- [@artigo@Regra de Três/Cinco/Zero](https://en.cppreference.com/w/cpp/language/rule_of_three.html)
- [@artigo@Regra de 0/3/5](https://medium.com/@Farhan11637/the-rule-of-0-3-5-2e608a717811)
