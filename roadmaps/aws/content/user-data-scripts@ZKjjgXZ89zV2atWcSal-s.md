# Scripts de Dados do Usuário

"Scripts de Dados do Usuário" em instâncias EC2 são usados para realizar tarefas de configuração automatizada comuns e até mesmo executar scripts após a inicialização da instância. Esses scripts são executados como o usuário root e podem ser usados para instalar software ou baixar arquivos de um bucket S3. Você pode passar até 16 KB de dados para uma instância, seja em formato de texto simples ou codificado em base64. O script de Dados do Usuário é executado apenas uma vez quando a instância é inicializada pela primeira vez. Se você parar e reiniciar a instância, o script não será executado novamente. No entanto, ele será executado em cada inicialização se a instância reiniciar.

Acesse os seguintes recursos para saber mais:

- [@official@Scripts de Dados do Usuário EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
