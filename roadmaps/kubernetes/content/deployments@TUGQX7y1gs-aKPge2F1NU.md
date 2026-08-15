# Implantações

Um Deployment é um objeto de recurso para gerenciar Pods e ReplicaSets por meio de uma configuração declarativa, que define um estado desejado que descreve o ciclo de vida do trabalho de aplicação, número de pods, estratégias de implantação, imagens de contêiner e muito mais. O Controlador Deployment trabalha para garantir que o estado atual corresponda ao estado desejado, como substituindo um pod falhante. Por padrão, as Implantações suportam várias estratégias de implantação, como "recreate" e "rolling update", mas podem ser personalizadas para suportar estratégias de implantação mais avançadas como blue/green ou canary.

Acesse os seguintes recursos para saber mais:

- [@oficial@Documentação de Implantações](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [@artigo@Implantação do Kubernetes: De Estratégias Básicas a Entrega Progressiva](https://codefresh.io/learn/kubernetes-deployment/)
- [@vídeo@Implantações do Kubernetes | Estratégias de Implantação](https://youtu.be/lxc4EXZOOvE)
