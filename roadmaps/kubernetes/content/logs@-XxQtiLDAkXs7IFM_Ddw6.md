# Logs

Os logs são gerados por aplicativos containerizados em execução nos nós dentro do cluster. Você pode acessar esses logs usando o comando kubectl logs seguido pelo nome do pod. Por padrão, esse comando exibe os logs do contêiner mais recente no pod, mas você pode especificar um contêiner específico dentro do pod adicionando o nome do contêiner ao comando. Adicionar a flag -f ao comando permite que você siga os logs em tempo real. Também estão disponíveis soluções de log de terceiros para Kubernetes, como as pilhas EFK e Prometheus, que fornecem capacidades avançadas de log e escalabilidade para aplicativos de escala maior.

Acesse os seguintes recursos para saber mais:

- [@oficial@Logs do Sistema](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/)
- [@video@Kubernetes: Explicação da coleta de logs](https://www.youtube.com/watch?v=6kmHvXdAzIM)
