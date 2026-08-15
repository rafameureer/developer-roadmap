# Perfil de Instância

Perfis de instância são entidades do AWS IAM que você pode usar para conceder permissões a aplicativos em execução nas suas instâncias EC2. Eles permitem efetivamente que as instâncias façam solicitações de API seguras. Um perfil de instância é essencialmente um contêiner para uma função do AWS Identity and Access Management (IAM) que você pode usar para passar funções às instâncias EC2 no momento da inicialização. Uma vez que uma função IAM seja associada a uma instância no momento da inicialização, não podemos alterar a função. No entanto, você pode modificar as políticas de permissões anexadas à função, e as permissões atualizadas entram em vigor imediatamente.

Acesse os seguintes recursos para saber mais:

- [@official@Perfis de Instância](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)
