# Tabelas Virtuais

Tabelas virtuais (vtables) são tabelas de pesquisa geradas pelo compilador em C++ para implementar o polimorfismo dinâmico, especialmente com funções virtuais. Cada classe que declara ou herda funções virtuais tem uma vtable, que contém ponteiros para as versões mais derivadas dessas funções virtuais para aquela classe. Quando uma função virtual é chamada através de um ponteiro ou referência a uma classe base, a vtable é consultada em tempo de execução para determinar a função real a ser executada com base no tipo dinâmico do objeto.

Acesse os seguintes recursos para saber mais:

- [@article@Entendendo Tabelas Virtuais em C++](https://pabloariasal.github.io/2017/06/10/understanding-virtual-tables/)
- [@video@Classes part 18 - Entendendo a vtable (Pergunta de entrevista popular) | Série Modern Cpp Ep. 54](https://www.youtube.com/watch?v=hS7kPtVB1vI)
