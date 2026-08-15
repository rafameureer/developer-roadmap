# Usuários / Permissões de Grupos

Os usuários, grupos e permissões de arquivos do Linux controlam o acesso a arquivos e recursos no sistema. No Docker, entender esses conceitos é importante porque os contêineres executam processos como usuários específicos, e o modelo de permissões determina quais arquivos uma aplicação contenedora pode ler, escrever ou executar. Por padrão, os contêineres são executados como root, o que apresenta riscos de segurança, então é uma boa prática criar usuários não-root em seu Dockerfile usando `RUN useradd` e alternar para eles com a instrução `USER`. Comandos como `chmod`, `chown` e `chgrp` ajudam você a definir as permissões corretas nos arquivos e diretórios dentro das imagens de contêiner.

Acesse os seguintes recursos para saber mais:

- [@artigo@Permissões de Arquivos no Linux Explicadas](https://www.redhat.com/en/blog/linux-file-permissions-explained)
- [@artigo@Usuários e Grupos no Linux](https://wiki.archlinux.org/title/Users_and_groups)
- [@oficial@Instrução USER do Dockerfile](https://docs.docker.com/reference/dockerfile/#user)
- [@feed@Explore os melhores posts sobre Docker](https://app.daily.dev/tags/docker?ref=roadmapsh)
