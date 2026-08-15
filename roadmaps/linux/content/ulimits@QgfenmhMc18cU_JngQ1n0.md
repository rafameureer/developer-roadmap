# Ulimits

Os ulimits (limites de usuário) são recursos do kernel Linux que restringem os recursos como handles de arquivo e memória que os processos podem consumir. Na contêinerização, os ulimits impedem que processos maliciosos esgotem recursos do servidor e criem situações de negação de serviço. Use `ulimit -a` para exibir limites atuais e `ulimit -n 1024` para definir limites específicos para um desempenho ótimo e segurança dos contêineres.

Acesse os seguintes recursos para saber mais:

- [@article@Verifique e defina limites de usuário com o comando ulimit Linux](https://linuxconfig.org/limit-user-environment-with-ulimit-linux-command)
- [@article@Como Usar o Comando Ulimit no Linux](https://linuxhandbook.com/ulimit-command/)
- [@article@10 Dicas de Solução de Problemas do Linux](https://www.dummies.com/article/technology/computers/operating-systems/linux/10-linux-troubleshooting-tips-274301/)
