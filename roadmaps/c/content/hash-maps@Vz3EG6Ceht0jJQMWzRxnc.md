# Hash Maps

Os hash maps armazenam pares chave-valor e usam uma função de hash para converter cada chave em um índice em um array subjacente, permitindo uma busca, inserção e exclusão em tempo constante médio. Como C não tem um mapa de hash embutido, implementá-lo envolve escrever uma função de hash, lidar com colisões quando duas chaves têm o mesmo índice e gerenciar a redimensionamento do array subjacente. Estratégias comuns para lidar com colisões incluem encadeamento, onde entradas colidindo formam uma lista vinculada, e endereçamento aberto, onde o mapa procura pelo próximo slot livre.

Acesse os seguintes recursos para saber mais:

- [@article@Como implementar uma tabela de hash (em C)](https://benhoyt.com/writings/hash-table-in-c/)
- [@video@Entendendo e implementando uma Tabela de Hash (em C)](https://www.youtube.com/watch?v=2Ti5yvumFTU)
