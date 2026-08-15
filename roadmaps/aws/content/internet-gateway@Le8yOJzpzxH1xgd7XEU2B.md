# Gateway da Internet

Um **Gateway da Internet** é um componente redundante e escalável horizontalmente na AWS que realiza roteamento bidirecional entre uma VPC e a Internet. Ele serve dois propósitos; rotear o tráfego de saída da VPC para a internet (NAT), e rotear o tráfego de entrada da Internet para a VPC. Ele é automaticamente altamente disponível e fornece largura de banda e redundância em todas as regiões da AWS. Ele se associa a uma VPC na criação, e não pode ser desassociado ou reassociado a outra VPC uma vez criado. A segurança para e do Gateway da Internet pode ser controlada usando tabelas de roteamento e grupos de segurança ou ACLs de rede.

Acesse os seguintes recursos para saber mais:

- [@artigo@Gateway da Internet](https://www.cisco.com/c/en/us/products/routers/what-is-a-network-gateway.html)
