# Idempotência

Idempotência é um conceito crucial em IaC. Uma operação idempotente produz o mesmo resultado independentemente de quantas vezes ela seja executada. No contexto de IaC, isso significa que aplicar a mesma configuração várias vezes não deve alterar o estado final do sistema. O papel da idempotência em scripts de IaC é garantir consistência e prevenir efeitos colaterais indesejados. Por exemplo, se um script para criar uma máquina virtual (VM) for executado duas vezes, ele não deve criar duas VMs. Em vez disso, ele deve reconhecer que a VM já existe e não tomar nenhuma ação.

Acesse os seguintes recursos para saber mais:

- [@artigo@Por que a idempotência foi importante para DevOps](https://dev.to/startpher/why-idempotence-was-important-to-devops-2jn3)
- [@artigo@Idempotência: O Segredo da Integração e Operações Semânticas](https://medium.com/@tiwari.sushil/idempotency-the-secret-to-seamless-devops-and-infrastructure-bf22e63e1be5)
