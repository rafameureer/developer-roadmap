# Docker Volumes

Volumes do Docker são soluções de armazenamento persistente usadas para gerenciar e armazenar dados fora do sistema de arquivos do contêiner, garantindo que os dados permaneçam intactos mesmo se o contêiner for excluído ou recém-criado. Eles são ideais para armazenar dados de aplicativos, logs e arquivos de configuração que precisam persistir em reinicializações e atualizações de contêineres. Com a CLI do Docker, você pode criar e gerenciar volumes usando comandos como `docker volume create` para definir um novo volume, `docker volume ls` para listar todos os volumes e `docker run -v` para montar um volume em um contêiner específico. Esse abordagem ajuda a manter a integridade dos dados, simplifica processos de backup e suporta compartilhamento de dados entre contêineres, tornando os volumes uma parte essencial de aplicativos containerizados com estado.

Acesse os seguintes recursos para saber mais:

- [@official@Docker Volumes](https://docs.docker.com/storage/volumes/)
- [@official@Docker Volume Commands](https://docs.docker.com/engine/reference/commandline/volume/)
