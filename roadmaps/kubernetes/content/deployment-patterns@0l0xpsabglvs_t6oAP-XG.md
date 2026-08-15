# Implantações Blue Green

É uma estratégia de implantação usada no Kubernetes para implantar novas versões de uma aplicação executando duas ambientes de produção idênticos, um com a versão atual (azul) e outro com a nova versão (verde). Após o ambiente verde ser completamente testado, o tráfego é roteado do ambiente azul para o ambiente verde, fornecendo uma transição suave para os usuários e evitando qualquer tempo de inatividade ou interrupção. No Kubernetes, as Implantações Blue-Green podem ser implementadas usando uma variedade de ferramentas e técnicas, incluindo estratégias de implantação, roteamento de tráfego e balanceamento de carga.

Acesse os seguintes recursos para saber mais:

- [@artigo@Criar uma Implantação Blue Green no Kubernetes](https://developer.harness.io/docs/continuous-delivery/cd-execution/kubernetes-executions/create-a-kubernetes-blue-green-deployment/)
- [@vídeo@Kubernetes - Implantações Blue/Green](https://www.youtube.com/watch?v=jxhpTGQ484Y)
