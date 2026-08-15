# Definindo solicitações e limites de recursos

As solicitações e limites de recursos no Kubernetes especificam a quantidade mínima e máxima de CPU e memória que um contêiner requer para funcionar. As solicitações são usadas para agendar contêineres em nós com recursos suficientes, enquanto os limites impõem cotas de recursos e impedem que os contêineres consumam muito. Essas configurações podem ser definidas no nível do pod ou do contêiner usando o campo resources no YAML. É importante definir solicitações e limites corretamente para garantir a utilização ótima dos recursos em seu cluster Kubernetes.

Acesse os seguintes recursos para saber mais:

- [@oficial@Solicitações e limites - Documentação](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits)
- [@oficial@Motivação para limites de memória padrão e solicitações](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/#motivation-for-default-memory-limits-and-requests)
- [@artigo@Entendendo os tipos de recursos do Kubernetes](https://thenewstack.io/understanding-kubernetes-resource-types/)
- [@artigo@Solicitações e limites do Kubernetes demistificados](https://thenewstack.io/kubernetes-requests-and-limits-demystified/)
