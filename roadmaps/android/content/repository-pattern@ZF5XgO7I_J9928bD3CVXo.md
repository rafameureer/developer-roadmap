# Padrão de Repositório

O `Padrão de Repositório` separa as fontes de dados da restante da aplicação. Ele atua como um mediador entre diferentes fontes de dados, como modelos persistentes, serviços web ou caches. Em vez de ter chamadas de rede e banco de dados espalhadas por toda a ViewModel, elas são encapsuladas em uma classe de Repositório. Esta separação tornará o código limpo, fácil de ler e testável. Ele fornece uma API simples para acesso aos dados, a restante da aplicação não precisa saber onde os dados estão vindo; ela apenas solicita ao repositório.

Acesse os seguintes recursos para saber mais:

- [@article@Padrão de Repositório](https://en.wikipedia.org/wiki/Repository_pattern)
