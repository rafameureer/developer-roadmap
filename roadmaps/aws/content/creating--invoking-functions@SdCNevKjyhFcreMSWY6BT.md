# Criando / Invocando Funções

Para criar uma função Lambda no AWS, navegue para a AWS Management Console, selecione "Lambda" em "Compute" e depois "Create function". Especifique o nome da função, papel de execução e ambiente de tempo de execução. Uma vez que a função for criada, você pode escrever ou colar o código no editor embutido. Para invocar uma função Lambda, você pode fazer isso manualmente, via API Gateway ou agendando-a. A invocação manual pode ser feita selecionando sua função na console AWS, em seguida "Test", adicionando o JSON do evento e testando novamente. Se configurado com um API Gateway, será acionado quando os endpoints forem atingidos. Agendar envolve usar o AWS CloudWatch para disparar as funções periodicamente.

Acesse os seguintes recursos para saber mais:

- [@oficial@Criar Sua Primeira Função Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
- [@vídeo@Sua Primeira Função Lambda AWS](https://www.youtube.com/watch?v=e1tkFsFOBHA)
