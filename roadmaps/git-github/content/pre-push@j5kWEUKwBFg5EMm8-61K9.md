# pre-push

O gatilho `pre-push` é executado antes de commits serem empurrados para um repositório remoto, permitindo que verifiquem os commits que estão prestes a ser compartilhados. Ele é frequentemente usado para rodar uma suite de testes ou verificar se a branch está atualizada antes de permitir o envio do push. Se o script sair com um status não-zero, o push será cancelado.

Acesse os seguintes recursos para saber mais:

- [@article@Gatilhos pre-push](https://dev.to/jameson/pre-push-hooks-42g5)
- [@video@Detectando segredos com um gatilho git pre-commit](https://www.youtube.com/watch?v=8bDKn3y7Br4)
