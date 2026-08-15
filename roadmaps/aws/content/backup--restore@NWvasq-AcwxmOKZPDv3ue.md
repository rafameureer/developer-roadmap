# Backup / Restore

No AWS, o DynamoDB possui suporte embutido para recursos de backup e restauração de dados. Isso inclui tanto backups demanda como backups contínuos. Os backups demanda permitem que você crie cópias completas das suas tabelas para retenção a longo prazo e arquivamento, ajudando a atender aos requisitos regulatórios corporativos e governamentais. Os backups contínuos permitem restaurar os dados da tabela em qualquer ponto no tempo nos últimos 35 dias, oferecendo proteção contra escritas ou exclusões acidentais. Durante uma operação de restauração, você pode escolher restaurar os dados para uma nova tabela do DynamoDB ou sobrescrever dados em uma tabela existente. Esses backups incluem todas as metadados necessários, incluindo índices secundários globais do DynamoDB.

Acesse os seguintes recursos para saber mais:

- [@official@Backup & Restore](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Backup-and-Restore.html)
