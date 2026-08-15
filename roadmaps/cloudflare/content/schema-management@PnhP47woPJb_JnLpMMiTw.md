# Gerenciamento de Esquema

Gerenciar a estrutura do seu banco de dados no Cloudflare D1 envolve definir tabelas, colunas, tipos de dados, chaves primárias, chaves estrangeiras e índices usando instruções padrão SQL Data Definition Language (DDL). Como o D1 é baseado em SQLite, você usará a sintaxe compatível com SQLite. Ferramentas como `wrangler` fornecem comandos para executar scripts SQL, permitindo que você crie e modifique seu esquema de banco de dados. Geralmente, começará projetando o esquema com base nas necessidades de dados da sua aplicação e depois traduzirá esse projeto em instruções DDL SQL. É importante dar atenção aos tipos de dados para garantir a integridade dos dados e a eficiência.

Acesse os seguintes recursos para saber mais:

- [@oficial@Validação de Esquema · Cloudflare API Shield](https://developers.cloudflare.com/api-shield/security/schema-validation/)
- [@oficial@Configurar Validação de Esquema · Cloudflare API Shield](https://developers.cloudflare.com/api-shield/security/schema-validation/configure/)
