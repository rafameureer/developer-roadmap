# Gateway NAT

O AWS NAT Gateway é um serviço gerenciado que fornece tradução de endereço de rede fonte (NAT) para as instâncias em uma sub-rede privada, permitindo que elas acessem a internet com segurança. Ele está projetado para operar automaticamente, lidando com escalonamento de largura de banda, failover e gerenciamento de endereços IP do provedor de serviços. Com o NAT Gateway, as instâncias dentro de um VPC podem acessar a internet para atualizações de software, patches, etc., mas o tráfego de entrada da internet é previsto, ajudando a manter a segurança e a privacidade da sub-rede privada. O NAT Gateway é redundante na Zona de Disponibilidade, fornecendo alta disponibilidade. Ele suporta os protocolos TCP, UDP e ICMP, bem como a Tradução de Endereço de Porta (PAT).

Acesse os seguintes recursos para saber mais:

- [@official@Gateway NAT](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
