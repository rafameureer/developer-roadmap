# Executando Contêineres

O comando `docker run` cria e inicia um novo contêiner a partir de uma imagem especificada. Ele combina as operações `docker create` e `docker start`, oferecendo uma variedade de opções para personalizar o ambiente de execução do contêiner. Os usuários podem definir variáveis de ambiente, mapear portas e volumes, definir conexões de rede e especificar limites de recursos. O comando suporta modo desassociado para execução em segundo plano, modo interativo para acesso ao shell e a capacidade de substituir o comando padrão definido na imagem. As flags comuns incluem `-d` para modo desassociado, `-p` para mapeamento de portas, `-v` para montagem de volumes e `--name` para atribuir um nome de contêiner personalizado. Entender `docker run` é fundamental para implantar e gerenciar efetivamente os contêineres Docker.

Acesse os seguintes recursos para saber mais:

- [@oficial@Docker Run](https://docs.docker.com/engine/reference/commandline/run/)
