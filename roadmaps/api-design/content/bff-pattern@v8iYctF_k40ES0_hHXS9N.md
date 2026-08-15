# Padrão BFF

O padrão Backend for Frontend (BFF) envolve a criação de uma camada de API dedicada para cada tipo de cliente, geralmente um BFF para web, outro para móveis e possivelmente um para consumidores terceiros. Em vez de forçar todos os clientes a usar uma única API genérica, cada BFF é personalizado para a forma exata de dados e padrões de interação que seu cliente precisa. Isso reduz o sobre-carregamento de dados, simplifica a lógica do cliente e permite que cada equipe de frontend evolua seu contrato de API independentemente, sem afetar outros clientes.

Acesse os seguintes recursos para saber mais:

- [@artigo@Backend for Frontend](https://bff-patterns.com/)
- [@vídeo@"Backends for Frontends": o que é?](https://www.youtube.com/watch?v=tmGnpU8xOGE)
