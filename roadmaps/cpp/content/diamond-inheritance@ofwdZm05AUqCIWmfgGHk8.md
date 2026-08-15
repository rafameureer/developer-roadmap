# Herança Diamante

A herança diamante ocorre em C++ quando uma classe herda de múltiplas classes que, por sua vez, herdam de uma classe base comum, criando uma hierarquia em forma de diamante. Isso pode levar a ambiguidade porque a classe derivada herda várias cópias dos membros da classe base. Para resolver esse problema, é usado o uso de herança virtual, garantindo que apenas uma instância da classe base exista na classe derivada final, eliminando a ambiguidade e garantindo o acesso adequado aos membros.

Acesse os seguintes recursos para saber mais:

- [@artigo@Entendendo Herança Virtual e o Problema do Diamante em C++](https://medium.com/@antilogatharv/understanding-virtual-inheritance-and-the-diamond-problem-in-c-da7c63d76723)
