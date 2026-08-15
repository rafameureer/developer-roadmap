# Ciclos de Vida

No [ASP.NET](http://ASP.NET), os ciclos de vida da injeção de dependência (DI) determinam a duração dos objetos que são resolvidos através do contêiner DI. Existem várias opções de ciclo de vida pré-definidas na biblioteca `Microsoft.Extensions.DependencyInjection`, incluindo:

*   **Transient:** Um novo objeto é criado toda vez que ele é solicitado.
*   **Scoped:** Um novo objeto é criado para cada solicitação dentro do mesmo escopo.
*   **Singleton:** Um único objeto é criado e compartilhado em todo o aplicativo.

Além disso, você também pode criar um ciclo de vida personalizado implementando a interface `Microsoft.Extensions.DependencyInjection.IServiceScopeFactory`.

Acesse os seguintes recursos para saber mais:

- [@artigo@O que são Ciclos de Vida dos Serviços no ASP.NET Core?](https://endjin.com/blog/2022/09/service-lifetimes-in-aspnet-core)
- [@artigo@Aprenda sobre Ciclos de Vida dos Serviços no .NET Core](https://henriquesd.medium.com/dependency-injection-and-service-lifetimes-in-net-core-ab9189349420)
- [@vídeo@Guia Completo sobre os Ciclos de Vida da Injeção de Dependência](https://www.youtube.com/watch?v=wA5bPsv2CLA)
