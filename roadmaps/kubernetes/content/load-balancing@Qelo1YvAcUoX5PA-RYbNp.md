# Balanceamento de Carga

O balanceamento de carga distribui o tráfego de rede em vários pods ou nós usando um objeto Service. Um Service fornece um endpoint de rede estável para um conjunto de pods, permitindo que outros pods ou clientes externos acessem esses pods através de uma única endereço IP e nome DNS. O Kubernetes oferece três tipos de algoritmos de balanceamento de carga para os Services, que distribuem o tráfego com base em round-robin, menos conexões ou hash de IP. O balanceamento de carga é uma parte essencial da rede do Kubernetes, fornecendo distribuição eficiente e confiável de tráfego em um cluster.

Acesse os seguintes recursos para saber mais:

- [@oficial@Balanceamento de Carga - Documentação](https://kubernetes.io/docs/concepts/services-networking/ingress/#load-balancing)
- [@article@Ingress Controllers: The Swiss Army Knife of Kubernetes](https://thenewstack.io/ingress-controllers-the-swiss-army-knife-of-kubernetes/)
- [@video@Tutorial | Balanceamento de Carga Service no Kubernetes](https://www.youtube.com/watch?v=xCsz9IOt-fs)
