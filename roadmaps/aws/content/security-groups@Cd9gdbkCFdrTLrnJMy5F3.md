# Grupos de Segurança

Os Grupos de Segurança no AWS atuam como um firewall virtual para sua instância para controlar o tráfego de entrada e saída. Quando você lança uma instância em uma VPC, pode atribuir até cinco grupos de segurança à instância. Os Grupos de Segurança são stateful — se você enviar uma solicitação da sua instância, a resposta ao tráfego dessa solicitação é permitida a fluir independentemente das regras de segurança de entrada. Você pode especificar regras de permissão, mas não regras de negação. Você pode especificar regras separadas para o tráfego de entrada e saída. Portanto, se você precisar permitir uma comunicação específica entre suas instâncias, você precisará configurar tanto as regras de saída quanto as regras de entrada dos grupos de segurança remetente.

Acesse os seguintes recursos para saber mais:

- [@official@Grupos de Segurança](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
