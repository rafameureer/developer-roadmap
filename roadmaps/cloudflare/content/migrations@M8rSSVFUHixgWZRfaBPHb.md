# Migrações

À medida que sua aplicação evolui, o esquema do seu banco de dados provavelmente precisará ser alterado. As migrações de banco de dados fornecem uma maneira estruturada de aplicar essas alterações de forma controlada e repetível. No D1, você geralmente escreverá scripts SQL que contenham as instruções `ALTER TABLE` necessárias para modificar o esquema (por exemplo, adicionando novas colunas, renomeando colunas, alterando tipos de dados). Em seguida, poderá usar `wrangler` ou uma ferramenta semelhante para executar esses scripts de migração em seu banco de dados D1. É importante versão controlar seus scripts de migração e aplicá-los na ordem correta para evitar inconsistências de dados ou erros. Considere usar uma ferramenta de gerenciamento de migrações para rastrear e aplicar migrações de forma mais eficaz.

Acesse os seguintes recursos para saber mais:

- [@artigo@ Migrações de Banco de Dados: Quais são os Tipos de Migrações de DB?](https://www.prisma.io/dataguide/types/relational/what-are-database-migrations)
- [@artigo@ Migrações de Banco de Dados no Mundo Real](https://blog.jetbrains.com/idea/2025/02/database-migrations-in-the-real-world/)
