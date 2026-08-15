# Adicionar / Atualizar

Para adicionar um submódulo a um repositório, use `git submodule add https://github.com/user/submodule-repo.git`, que é o formato típico para especificar a URL do repositório de submódulo. Isso cria uma nova pasta para o submódulo e o verifica na revisão especificada. Para atualizar um submódulo existente para seu último commit, execute `git submodule update`. Se você quiser puxar alterações da origem enquanto mantém a história do submódulo intacta, use `git submodule sync` seguido por `git submodule update`.

Acesse os seguintes recursos para saber mais:

- [@artigo@Submódulos do Git](https://www.atlassian.com/git/tutorials/git-submodule)
- [@artigo@Trabalhando com submódulos](https://github.blog/open-source/git/working-with-submodules/)
