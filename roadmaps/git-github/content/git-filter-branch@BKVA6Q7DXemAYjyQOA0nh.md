# git filter-branch

O comando `git filter-branch` reescreve uma grande parte da história de um repositório, frequentemente usado para remover arquivos sensíveis ou reestruturar o projeto posteriormente. Ele aplica um filtro em muitos ou todos os commits, como deletar um arquivo específico em todo o histórico. Por ser lento e propenso a erros, a documentação do Git agora recomenda a ferramenta `git filter-repo` como uma alternativa mais rápida e segura para o mesmo tipo de reescrita de história.

Acesse os seguintes recursos para saber mais:

- [@official@git filter-branch](https://git-scm.com/docs/git-filter-branch)
- [@official@git filter-repo](https://github.com/newren/git-filter-repo)
- [@article@Removendo dados sensíveis de um repositório](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
