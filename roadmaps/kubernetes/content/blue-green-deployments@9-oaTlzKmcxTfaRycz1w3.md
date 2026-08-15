# Implantações Blue-Green

É uma estratégia de implantação usada em Kubernetes para implantar novas versões de um aplicativo ao executar dois ambientes de produção idênticos, um com a versão atual (azul) e outro com a nova versão (verde). Após o ambiente verde ser totalmente testado, o tráfego é direcionado do ambiente azul para o ambiente verde, fornecendo uma transição suave para os usuários e evitando qualquer tempo de inatividade ou interrupção. No Kubernetes, as Implantações Blue-Green podem ser implementadas usando uma variedade de ferramentas e técnicas, incluindo estratégias de implantação, roteamento de tráfego e balanceamento de carga.

Acesse os seguintes recursos para saber mais:

- [@article@Criar uma Implantação Blue-Green do Kubernetes](https://developer.harness.io/docs/continuous-delivery/cd-execution/kubernetes-executions/create-a-kubernetes-blue-green-deployment/)
- [@video@Kubernetes - Implantações Blue/Green](https://www.youtube.com/watch?v=jxhpTGQ484Y)
