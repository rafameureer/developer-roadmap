# Taints e Tolerations

Taints (tinturas) e tolerations são usados no Kubernetes para restringir ou permitir que os pods sejam agendados em certos nós com base em rótulos. Uma tinta é um rótulo aplicado a um nó para indicar determinadas limitações ou requisitos. Uma toleração é um rótulo aplicado a um pod para indicar que ele pode tolerar determinadas tintas. Quando um nó tem uma tinta, apenas os pods com as correspondentes tolerações podem ser agendados nesse nó. Esta funcionalidade é útil para diversos propósitos, como garantir a separação de cargas de trabalho críticas e não-criticas, reservar nós para certos trabalhos e proteger nós da sobrecarga.

Acesse os seguintes recursos para saber mais:

- [@oficial@Taints e Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
- [@vídeo@Kubernetes Para Iniciantes: Taints & Tolerations](https://www.youtube.com/watch?v=mo2UrkjA7FE)
