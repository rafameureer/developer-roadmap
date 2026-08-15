# Básicos do Docker

O Docker é uma plataforma que simplifica a construção, empacotamento e implantação de aplicativos em contêineres leves e portáteis. Componentes-chave incluem Dockerfiles (instruções de build), Imagens (capturas instantâneas) e Contêineres (instâncias em execução). Comandos essenciais cobrem o download de imagens, a construção a partir de Dockerfiles, a execução de contêineres com mapeamento de portas e a gestão tanto dos contêineres quanto das imagens.

O que é um Contêiner?
--------------------

Um contêiner é um pacote leve, independente e executável de software que inclui todas as dependências (bibliotecas, binários e arquivos de configuração) necessárias para executar um aplicativo. Os contêineres isolam aplicativos do seu ambiente, garantindo que eles funcionem consistentemente em diferentes sistemas.

Componentes do Docker
---------------------

Existem três componentes-chave no ecossistema do Docker:

*   **Dockerfile**: Um arquivo de texto contendo instruções (comandos) para construir uma imagem do Docker.
*   **Imagem do Docker**: Uma captura instantânea de um contêiner, criada a partir de um Dockerfile. As imagens são armazenadas em um registro, como o Docker Hub, e podem ser-puxadas ou empurradas para o registro.
*   **Contêiner do Docker**: Uma instância em execução de uma imagem do Docker.

Comandos do Docker
---------------

Abaixo estão alguns comandos do Docker essenciais que você usará frequentemente:

*   `docker pull <image>`: Baixe uma imagem de um registro, como o Docker Hub.
*   `docker build -t <nome_da_imagem> <caminho>`: Construa uma imagem a partir de um Dockerfile, onde `<caminho>` é o diretório contendo o Dockerfile.
*   `docker image ls`: Liste todas as imagens disponíveis em seu computador local.
*   `docker run -d -p <porta_do_host>:<porta_do_contêiner> --name <nome_do_contêiner> <image>`: Execute um contêiner a partir de uma imagem, mapeando portas do host para as portas do contêiner.
*   `docker container ls`: Liste todos os contêineres em execução.
*   `docker container stop <contêiner>`: Pare um contêiner em execução.
*   `docker container rm <contêiner>`: Remova um contêiner parado.
*   `docker image rm <image>`: Remova uma imagem do seu computador local.
