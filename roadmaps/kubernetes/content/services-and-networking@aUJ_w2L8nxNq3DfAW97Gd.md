# Comunicação de rede e comunicação entre pods

A comunicação de rede é crucial para a interação entre os pods e recursos em um cluster Kubernetes. Cada pod tem um endereço IP único e pode se comunicar diretamente com outros pods. Os plug-ins do Container Networking Interface (CNI) são usados para configurar as interfaces de rede dos pods e fornecer isolamento entre eles. O Kubernetes também fornece serviços de rede como balanceamento de carga, descoberta de serviço e ingresso, que permitem que o tráfego externo acesse os pods e serviços. Esses serviços são implementados usando objetos do Kubernetes como Serviços, Ingress e NetworkPolicies. A comunicação de rede e a comunicação entre pods são essenciais para a escalabilidade, confiabilidade e flexibilidade dos clusters Kubernetes.

Acesse os seguintes recursos para saber mais:

- [@oficial@Rede de cluster - Documentação](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- [@oficial@Trabalhando com comunicação entre pods em um job](https://kubernetes.io/docs/tasks/job/job-with-pod-to-pod-communication/)
- [@artigo@Como o Kubernetes fornece rede e armazenamento para as aplicações](https://thenewstack.io/how-kubernetes-provides-networking-and-storage-to-applications/)
- [@feed@Explore top posts about Networking](https://app.daily.dev/tags/networking?ref=roadmapsh)
