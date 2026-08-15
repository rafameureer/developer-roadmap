# JavaScript

O tipo de dados JavaScript no MongoDB permite que você armazene código JavaScript como valores BSON em documentos, permitindo a execução de funções JavaScript do lado do servidor para operações como map-reduce, procedimentos armazenados e transformações de dados complexas. Esse tipo pode armazenar funções JavaScript ou trechos de código que podem ser executados no ambiente do servidor MongoDB, tornando-o útil em cenários onde você precisa realizar cálculos complexos, lógica de negócios personalizada ou operações de agregação personalizadas diretamente no servidor de banco de dados. No entanto, o tipo JavaScript é principalmente uma funcionalidade legada e geralmente não é recomendado em aplicativos modernos do MongoDB devido a preocupações de segurança e implicações de desempenho, com o framework de agregação sendo a abordagem preferida para tarefas de processamento de dados complexas que anteriormente exigiam execução de JavaScript do lado do servidor.

Acesse os seguintes recursos para saber mais:

- [@official@Javascript Function on Server](https://www.mongodb.com/docs/manual/tutorial/store-javascript-function-on-server/)
- [@article@Unleash Data Magic with MongoDB Custom JavaScript Functions](https://thelinuxcode.com/mongodb-custom-function/)
