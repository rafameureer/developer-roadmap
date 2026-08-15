# Sistema de Arquivos Ephemeral

Por padrão, o armazenamento dentro de um contêiner do Docker é efêmero, o que significa que quaisquer alterações ou modificações feitas dentro de um contêiner só persistirão até que o contêiner seja parado e removido. Uma vez que o contêiner for parado e removido, todos os dados associados serão perdidos. Isso ocorre porque os contêineres do Docker são projetados para serem sem estado por natureza. Este armazenamento temporário ou de curta duração é chamado de "sistema de arquivos efêmero" dos contêineres. É uma característica essencial do Docker, pois permite a implantação rápida e consistente de aplicativos em diferentes ambientes sem se preocupar com o estado de um contêiner.

Acesse os seguintes recursos para saber mais:

- [@official@Persistência de Dados - Documentação do Docker](https://docs.docker.com/get-started/docker-concepts/running-containers/persisting-container-data/)
- [@video@Conceitos do Docker - Persistindo dados dos contêineres](https://www.youtube.com/watch?v=10_2BjqB_Ls)
