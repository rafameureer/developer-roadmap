# Baseado em Recursos

Políticas baseadas em recursos são anexadas diretamente aos recursos AWS que recebem permissões. A política, então, especifica quais ações são permitidas ou negadas nesse recurso específico. Em políticas baseadas em recursos, você inclui um elemento `Principal` na política para indicar os usuários IAM ou papéis que recebem as permissões. Embora não todos os serviços AWS suportem políticas baseadas em recursos, comuns incluem o Amazon S3 para políticas de bucket, o AWS KMS para políticas de chave e o Amazon SNS para políticas de tópico.

Acesse os seguintes recursos para saber mais:

- [@official@Políticas Baseadas em Identidade](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html)
