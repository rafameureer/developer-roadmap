# Cache do Entity Framework

Entity Framework Core (EF Core) é uma versão multiplataforma da popular tecnologia de acesso a dados Entity Framework que é leve, extensível e open source. Ele pode ser usado como um mapeador objeto-relacional (O/RM), permitindo aos desenvolvedores .NET usar objetos .NET para interagir com um banco de dados e removendo a necessidade da maioria do código de acesso a dados que geralmente é necessário.

No entanto, durante picos de carga, aplicativos .NET Core de alta transação usando EF Core têm problemas de desempenho e escalabilidade na camada de banco de dados. Isso ocorre porque, embora você possa escalar a camada de aplicativo adicionando mais servidores de aplicativo, não é possível escalar a camada de banco de dados adicionando mais servidores de banco de dados.

Acesse os seguintes recursos para saber mais:

- [@article@Cache do Entity Framework 2º nível](https://www.gridgain.com/docs/latest/developers-guide/net-specific/net-entity-framework-cache)
- [@article@Caching no Entity Framework](https://www.c-sharpcorner.com/article/caching-in-entity-framework-ef-core-using-ncache/)
- [@video@O que é o Entity Framework?](https://www.youtube.com/watch?v=Z7713GBhi4k)
