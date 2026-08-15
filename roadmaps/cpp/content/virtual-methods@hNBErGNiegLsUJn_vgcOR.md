# Métodos Virtuais

Métodos virtuais são a pedra angular da polimorfismo dinâmico em classes C++. Eles permitem que uma classe derivada forneça sua própria implementação específica de uma função que já está definida em uma classe base. Quando você chama uma função virtual através de um ponteiro ou referência de classe base, o tempo de execução determina qual versão da função executar com base no tipo real do objeto apontado, não no tipo do ponteiro ou referência em si. Este mecanismo, conhecido como despacho dinâmico, permite código flexível e extensível onde o comportamento pode ser ajustado em tempo de execução.

Acesse os seguintes recursos para saber mais:

- [@official@Documentação de Funções Virtuais em C++](https://en.cppreference.com/w/cpp/language/virtual)
- [@video@Funções Virtuais Explained (YouTube)](https://www.youtube.com/watch?v=oIV2KchSyGQ&ab_channel=TheCherno)
