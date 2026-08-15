# Espaço de Troca

O espaço de troca estende a memória física usando o armazenamento em disco quando a RAM está cheia. As páginas de memória inativas são movidas para o espaço de troca, liberando a RAM, mas com um impacto na performance devido ao acesso mais lento ao disco. O espaço de troca pode existir como partições dedicadas ou arquivos regulares. Crie com os comandos `fallocate`, `mkswap` e `swapon`. Crítico para o gerenciamento de memória e otimização da estabilidade do sistema.

Acesse os seguintes recursos para saber mais:

- [@artigo@Espaço de Troca - Wiki Arch](https://wiki.archlinux.org/title/Swap)
- [@artigo@Como Aumentar o Espaço de Troca no Linux](https://linuxconfig.org/how-to-increase-swap-space-on-linux)
