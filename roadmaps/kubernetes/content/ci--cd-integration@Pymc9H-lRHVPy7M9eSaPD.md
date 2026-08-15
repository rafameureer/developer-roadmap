# Integração CI/CD

No padrão CI/CD, a construção, teste e implantação de aplicativos no Kubernetes são totalmente automatizados. O pipeline CI cria a imagem do contêiner, executa testes e empurra para um registro. O pipeline CD então atualiza os manifestos do Kubernetes ou os gráficos Helm e os aplica ao cluster usando ferramentas como Octopus Deploy, Argo CD, Flux ou kubectl. Isso torna as implantações consistentes, repetíveis e rápidas.

Acesse os seguintes recursos para saber mais:

- [@artigo@Pipelines CI/CD do Kubernetes – 8 Melhores Práticas e Ferramentas](https://spacelift.io/blog/kubernetes-ci-cd)
- [@artigo@8 Ferramentas de CI/CD do Kubernetes que todos os desenvolvedores devem conhecer](https://octopus.com/devops/kubernetes-deployments/kubernetes-ci-cd-tools-for-developers/)
- [@artigo@Implantar no Kubernetes com o Octopus Deploy](https://octopus.com/use-case/kubernetes?utm_source=roadmap&utm_medium=link&utm_campaign=kubernetes-ci-cd-integration)
