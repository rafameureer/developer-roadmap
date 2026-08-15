# Blocos CIDR

"CIDR" significa Classless Inter-Domain Routing. No AWS VPC, um bloco CIDR é o bloco de endereços IP a partir do qual os endereços IPv4 privados e públicos são alocados quando você cria um VPC. O bloco CIDR pode variar de /28 (16 endereços IP) a /16 (65.536 endereços IP). Ele representa um segmento de rede e está associado com uma fronteira de rede. Ao criar, você não pode alterar o bloco CIDR do seu VPC, mas você pode adicionar blocos CIDR adicionais se necessário. O bloco CIDR de um VPC deve não overlappar com nenhum dos blocos CIDR existentes da rede.

Acesse os seguintes recursos para saber mais:

- [@oficial@cidr.xyz: Visualizador interativo de intervalos CIDR](https://cidr.xyz/)
- [@oficial@VPC - Blocos CIDR](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html)
