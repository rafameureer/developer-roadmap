# Prioridades de Pods

As prioridades de pods no Kubernetes determinam a ordem em que os pods são agendados nos nós quando há competição por recursos. Cada pod é atribuído a um valor numérico de prioridade, com valores mais altos indicando uma prioridade maior. O scheduler maximiza o valor total de prioridade dos pods agendados, considerando também a adequação do nó, tolerâncias e tolerações, regras de afinidade e anti-afinidade. As prioridades podem ser definidas manualmente ou automaticamente com base em lógica de negócios ou requisitos da aplicação. As prioridades ajudam a garantir que as cargas de trabalho críticas recebam os recursos necessários e sejam agendadas primeiro, enquanto as cargas de trabalho de menor prioridade são agendadas quando os recursos se tornarem disponíveis.

Acesse os seguintes recursos para saber mais:

- [@official@Prioridades de Pod - Documentação](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority)
- [@video@Prioridades de Pod no Kubernetes (Exemplos)](https://www.youtube.com/watch?v=sR_Zmvme3-0)
