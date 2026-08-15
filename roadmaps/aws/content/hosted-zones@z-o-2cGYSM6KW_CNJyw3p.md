# Zonas Hosted

Uma **Zona Hosted** no AWS Route 53 é essencialmente um contêiner que armazena informações sobre como você deseja direcionar o tráfego na internet para um domínio específico, como example.com. Cada zona hospedada está associada a um conjunto de registros DNS, que controlam o fluxo de tráfego para aquele domínio. O AWS Route 53 cria automaticamente um conjunto de registros que inclui um registro de servidor de nome (NS) e um registro de início de autoridade (SOA) quando você cria uma zona hospedada. Esses registros fornecem informações necessárias sobre seu domínio ao sistema DNS, estabelecendo a base para direcionar o tráfego para o endereço IP apropriado em seu ambiente AWS.

Acesse os seguintes recursos para saber mais:

- [@official@Zonas Hosted](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-working-with.html)
