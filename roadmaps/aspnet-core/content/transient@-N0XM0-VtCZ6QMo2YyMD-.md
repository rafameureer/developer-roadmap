# Transiente

A vida útil transiente é um tipo de injeção de dependência que cria uma nova instância de um objeto sempre que ele é solicitado. Isso significa que se vários componentes dentro da mesma solicitação ou em diferentes solicitações dependerem do mesmo serviço, cada um receberá uma nova instância do serviço.

A vida útil transiente é útil quando você tem serviços sem estado e não precisam manter nenhum dado entre as solicitações, como um serviço que realiza um cálculo simples ou retorna dados de um banco de dados.

Acesse os seguintes recursos para saber mais:

- [@artigo@O que são Dependências Transientes?](https://blazor-university.com/dependency-injection/dependency-lifetimes-and-scopes/transient-dependencies/)
- [@artigo@Vida útil da Injeção de Dependência](https://www.tektutorialshub.com/asp-net-core/asp-net-core-dependency-injection-lifetime/)
- [@vídeo@Injeção de Dependência Explicada com Transiente](https://www.youtube.com/watch?v=NkTF_6IQPiY)
