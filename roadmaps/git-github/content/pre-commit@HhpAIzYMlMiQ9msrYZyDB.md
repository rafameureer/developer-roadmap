# pre-commit

O gatilho `pre-commit` é executado antes de um commit ser finalizado, dando a oportunidade de inspecionar as alterações em stage e abortar o commit se algo estiver errado. Ele é frequentemente usado para rodar linters, formatadores ou testes contra o código que está sendo comitado. Se o script do gatilho sair com um status não-zero, o commit será interrompido.

Acesse os seguintes recursos para saber mais:

- [@official@Gatilhos Git](https://www.atlassian.com/git/tutorials/git-hooks)
- [@opensource@pre-commit/pre-commit](https://github.com/pre-commit/pre-commit)
