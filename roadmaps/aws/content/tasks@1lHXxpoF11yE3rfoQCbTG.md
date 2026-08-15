# Tarefas

As tarefas no Amazon ECS são a instância de uma definição de tarefa dentro de um cluster. Elas podem ser pensadas como a instância em execução da definição, da mesma forma que um objeto é uma instância de uma classe em programação orientada a objetos. Uma definição de tarefa é um arquivo de texto no formato JSON que descreve um ou mais contêineres, até um máximo de 10. Os parâmetros da definição de tarefa especificam a imagem do contêiner a ser usada, a quantidade de CPU e memória a ser alocada para cada contêiner e o tipo de lançamento a ser usado para a tarefa, entre outras opções. Quando uma tarefa é iniciada, ela é agendada em uma instância de contêiner disponível dentro do cluster.

Acesse os seguintes recursos para saber mais:

- [@official@Tarefas no ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html)
