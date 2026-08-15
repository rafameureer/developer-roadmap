# Capacidade e Crescimento

A capacidade de um slice determina quando ocorre a realocação durante operações de adição. Go geralmente duplica a capacidade para slices menores. Pré-aloque com `make([]T, comprimento, capacidade)` para otimizar o uso de memória e minimizar as alocações em código crítico de desempenho.

Acesse os seguintes recursos para saber mais:

- [@artigo@Entendendo a Estrutura de Dados Slice do Go e Seu Padrão de Crescimento](https://medium.com/@arjun.devb25/understanding-gos-slice-data-structure-and-its-growth-pattern-48fe6dd914b4)
- [@artigo@Como Aumentar a Capacidade de um Slice no Go](https://thekoreanguy.medium.com/how-does-the-capacity-change-when-you-append-to-a-slice-in-go-46289dad4730)
- [@artigo@Como Gerenciar Comprimento e Capacidade de um Slice](https://labex.io/tutorials/go-how-to-manage-slice-length-and-capacity-418932)
