# Serviços

Os serviços do Amazon ECS (Elastic Container Service) são definidos como um conjunto de parte ou todo de suas definições de tarefas que executam e mantêm um número especificado de instâncias de uma definição de tarefa simultaneamente em um cluster do Amazon ECS. Se qualquer uma das suas tarefas falhar ou parar por qualquer motivo, o agendador de serviços do Amazon ECS lançará outra instância da definição de tarefa para substituí-la e manter a contagem desejada de tarefas, garantindo a confiabilidade e disponibilidade do serviço. Os serviços ECS podem ser dimensionados manualmente ou com políticas de escalonamento automático baseadas em alarmes do CloudWatch. Além disso, as opções de agendamento de serviços ECS definem como o Amazon ECS coloca e termina tarefas.

Acesse os seguintes recursos para saber mais:

- [@oficial@Serviços no ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html)
