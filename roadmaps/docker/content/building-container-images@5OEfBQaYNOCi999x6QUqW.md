# Construindo Imagens de Contêiner

As imagens de contêiner são pacotes executáveis que incluem tudo o que é necessário para executar uma aplicação: código, tempo de execução, ferramentas do sistema, bibliotecas e configurações. Ao construir imagens personalizadas, você pode implantar aplicações de forma transparente com todas as suas dependências em qualquer plataforma suportada pelo Docker. O componente-chave na construção de uma imagem de contêiner é o `Dockerfile`. É essencialmente um script contendo instruções sobre como montar uma imagem do Docker. Cada instrução no Dockerfile cria uma nova camada na imagem, tornando mais fácil rastrear as alterações e minimizar o tamanho da imagem. Aqui está um exemplo simples de um Dockerfile:

Acesse os seguintes recursos para saber mais:

- [@oficial@Visão Geral do Build do Docker](https://docs.docker.com/build/concepts/overview)
- [@oficial@Construtor de Imagens do Docker](https://docs.docker.com/reference/cli/docker/buildx/build/)
- [@oficial@Referência do Dockerfile](https://docs.docker.com/engine/reference/builder/)
- [@opensource@Exemplos de Dockerfile](https://github.com/dockersamples)
