# StatefulSets

É um controlador que gerencia a implantação e escala de um conjunto de pods stateful que requerem identidades de rede estáveis e volumes de armazenamento estáveis. StatefulSets são usados para executar aplicativos stateful como bancos de dados, onde a ordem e unicidade de cada pod é importante. StatefulSets fornecem identidades de rede estáveis e volumes de armazenamento estáveis únicos para cada pod, o que permite que os aplicativos stateful mantenham a consistência dos dados mesmo quando são escalados para cima ou para baixo, ou quando nós falham ou são substituídos. StatefulSets são definidos por um arquivo YAML que inclui um modelo de pod, um serviço para acessar os pods e outras configurações.

Acesse os seguintes recursos para saber mais:

- [@oficial@Documentação dos StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [@artigo@Abordagens Diferentes para Construir Aplicações Kubernetes Stateful](https://thenewstack.io/different-approaches-for-building-stateful-kubernetes-applications/)
- [@vídeo@Kubernetes StatefulSet | Tutorial](https://www.youtube.com/watch?v=pPQKAR1pA9U)
