# Backup / Restore

`Backup Restore` no AWS RDS permite restaurar sua instância de banco de dados em um ponto específico no tempo. Quando você inicia uma restauração por pontos no tempo, uma nova instância de banco de dados é criada e todas as transações que ocorreram após o ponto no tempo especificado não fazem parte da nova instância de banco de dados. Você pode restaurar até a última hora restorable (geralmente dentro dos últimos cinco minutos) conforme indicado na Console de Gerenciamento do AWS RDS. O tempo que leva para criar a restauração depende da diferença no tempo entre quando você inicia a restauração e o momento em que está restaurando. O processo ocorre com nenhuma impacto na base de dados fonte e você pode continuar usando seu banco de dados durante a restauração.

Acesse os seguintes recursos para saber mais:

- [@official@Backup & Restore - RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html)
