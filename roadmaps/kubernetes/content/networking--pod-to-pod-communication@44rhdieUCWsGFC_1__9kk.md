# Networking & Comunicação entre Pods

O networking em Kubernetes permite que os pods se comuniquem uns com os outros dentro do cluster, independentemente do nó em que estão sendo executados. Cada pod é atribuído seu próprio endereço IP e o Kubernetes segue um modelo de rede plano onde todos os pods podem comunicar-se diretamente entre si sem a tradução de endereços de rede (NAT).

A comunicação entre pods é implementada por um **Container Network Interface (CNI)** plugin, como Calico, Flannel, Cilium ou Weave. Esses plugins são responsáveis pela atribuição de endereços IP, roteamento e aplicação de políticas de rede. Por padrão, todo o tráfego de pod é permitido, mas as **Políticas de Rede** podem ser usadas para controlar e restringir o tráfego entre pods para segurança e isolamento.

Uma comunicação confiável entre os pods é uma exigência essencial para a construção de aplicativos distribuídos e baseados em microserviços no Kubernetes.

Acesse os seguintes recursos para saber mais:

- [@official@Networking do Cluster - Documentação do Kubernetes](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- [@official@Políticas de Rede - Documentação do Kubernetes](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [@article@Explicando o Networking do Kubernetes](https://www.tigera.io/learn/guides/kubernetes-networking/)
- [@video@Visão Profunda sobre Networking do Kubernetes](https://www.youtube.com/watch?v=t98ekMiz0hQ)
