# Construtores CLI

Vários comandos do Angular CLI executam um processo complexo em seu código, como a construção, teste ou atendimento ao cliente da sua aplicação. Os comandos usam uma ferramenta interna chamada `Architect` para executar construtores CLI, que invocam outra ferramenta (empacotador, executador de testes, servidor) para concluir a tarefa desejada. Construtores personalizados podem realizar uma nova tarefa completamente ou alterar qual ferramenta terceirizada é usada por um comando existente.

Acesse os seguintes recursos para saber mais:

- [@official@Construtores CLI](https://angular.dev/tools/cli/cli-builder)
- [@opensource@Ferramentas de Construção do Angular](https://github.com/just-jeb/angular-builders)
- [@video@Angular Builders – Criando um Construtor Personalizado do Zero](https://www.youtube.com/watch?v=QbDkDLnXAZE)
