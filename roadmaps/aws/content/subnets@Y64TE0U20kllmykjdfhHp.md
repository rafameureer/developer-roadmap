# Subnets

Subnets ou sub-redes em Amazon VPC (Virtual Private Cloud) são divisões do intervalo de endereços IP da VPC. Você pode lançar instâncias do Amazon Elastic Compute Cloud (Amazon EC2) em uma sub-rede selecionada. Quando você cria uma sub-rede, especifica o bloco CIDR para a sub-rede, que é um subconjunto do bloco CIDR da VPC. Cada sub-rede deve ser associada a uma tabela de roteamento, que controla o fluxo de tráfego entre as sub-redes. Existem dois tipos de sub-redes: públicas e privadas. Uma sub-rede pública é aquela em que a tabela de roteamento associada direciona a sub-rede para a Internet Gateway (IGW) da VPC. Uma sub-rede privada não tem um caminho para o IGW e, portanto, não tem um caminho direto para a internet.

Acesse os seguintes recursos para saber mais:

- [@oficial@Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
