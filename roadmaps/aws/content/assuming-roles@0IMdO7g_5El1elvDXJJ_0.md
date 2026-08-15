# Suposição de Papéis

A suposição de papéis no AWS permite que uma identidade do AWS execute ações e acesse recursos em outra conta do AWS, sem ter que compartilhar credenciais de segurança. Isso é feito usando credenciais de segurança temporárias. Você assume um papel chamando as APIs `AWS Security Token Service (STS) AssumeRole`, passando o ARN do papel a ser assumido. Após assumir com sucesso um papel, STS retorna credenciais de segurança temporárias que você pode usar para fazer solicitações a qualquer serviço do AWS. O papel assumido fornece permissões específicas que determinam o que o usuário do papel pode e não pode fazer. Assim, os usuários podem alternar entre papéis usando o Console de Gerenciamento do AWS, CLI do AWS ou API do AWS.

Acesse os seguintes recursos para saber mais:

- [@oficial@Suposição de Papéis](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage-assume.html)
