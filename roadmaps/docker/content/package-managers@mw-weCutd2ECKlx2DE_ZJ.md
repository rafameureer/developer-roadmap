# Gerenciadores de Pacotes

Gerenciadores de pacotes são ferramentas usadas para instalar, atualizar e gerenciar pacotes de software em sistemas Linux. Como a maioria das imagens Docker é baseada em distribuições Linux, entender gerenciadores de pacotes como `apt` (Debian/Ubuntu), `yum`/`dnf` (RHEL/CentOS/Fedora) e `apk` (Alpine Linux) é essencial para construir imagens Docker. Em um Dockerfile, você geralmente usa instruções `RUN` com gerenciadores de pacotes para instalar as dependências necessárias pelo seu aplicativo, e é uma prática recomendada limpar caches de pacotes após isso para manter o tamanho da imagem pequeno.

Acesse os seguintes recursos para saber mais:

- [@article@Guia do Gerenciador de Pacotes APT](https://ubuntu.com/server/docs/package-management)
- [@article@Gerenciamento de Pacotes no Alpine Linux](https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper)
- [@video@Explicação dos Gerenciadores de Pacotes do Linux](https://www.youtube.com/watch?v=-iSMFoPPbKU)
- [@feed@Explore os melhores posts sobre Docker](https://app.daily.dev/tags/docker?ref=roadmapsh)
