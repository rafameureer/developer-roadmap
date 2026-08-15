# Segredos e Variáveis de Ambiente
 
Segredos armazenam valores sensíveis como chaves API ou senhas com segurança, configurados nas configurações do repositório e referenciados em fluxos sem expor seus valores reais nos logs. As variáveis de ambiente, definidas com a chave `env`, seguem valores de configuração que os passos em um fluxo podem acessar durante a execução. Ambas são usadas com frequência juntas, mantendo dados sensíveis fora do próprio arquivo de fluxo, mas ainda disponíveis onde necessário.

Acesse os seguintes recursos para saber mais:

- [@official@Usando segredos no GitHub Actions](https://docs.github.com/pt-br/actions/security-guides/using-secrets-in-github-actions)
- [@official@Armazenar informações em variáveis](https://docs.github.com/pt-br/actions/using-workflows/choosing-what-your-workflow-does/store-information-in-variables)
- [@video@Segredos e Variáveis de Ambiente no seu GitHub Action](https://www.youtube.com/watch?v=dPLPSaFqJmY)
