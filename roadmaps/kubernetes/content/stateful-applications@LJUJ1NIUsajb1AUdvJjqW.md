# Aplicações Stateful

No Kubernetes, o armazenamento é um componente chave para aplicativos stateful, pois esses aplicativos requerem armazenamento de dados persistente que esteja disponível em várias réplicas do aplicativo. O Kubernetes oferece várias opções de armazenamento, incluindo volumes, volumes persistentes e classes de armazenamento.

Volumes são os blocos básicos de construção de armazenamento no Kubernetes. Um volume é um diretório acessível ao contêiner que está executando o aplicativo, e ele pode ser suportado por diferentes tipos de armazenamento, como um diretório do host, um disco do provedor de nuvem ou um sistema de armazenamento de rede. Volumes são criados e gerenciados pelo Kubernetes e podem ser montados em contêineres como parte da definição de um pod.

Acesse os seguintes recursos para saber mais:

- [@oficial@Aplicações Stateful](https://kubernetes.io/docs/tutorials/stateful-application/)
- [@vídeo@Os fundamentos das aplicações stateful no Kubernetes](https://www.youtube.com/watch?v=GieXzb91I40)
