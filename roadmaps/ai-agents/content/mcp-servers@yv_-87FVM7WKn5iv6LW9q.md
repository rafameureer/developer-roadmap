# Servidores MCP

Um Servidor MCP é a máquina principal ou serviço em nuvem que executa o Protocolo de Contexto do Modelo. Ele mantém a memória compartilhada "que" diferentes agentes de IA precisam para manter-se na mesma página. Quando um agente envia uma solicitação, o servidor verifica quem está solicitando, puxa o contexto certo de seu armazenamento e o retorna rapidamente. Ele também salva novas fatos e resultados de tarefas para que o próximo agente possa usá-los. Um Servidor MCP deve lidar com muitos usuários ao mesmo tempo, proteger dados privados com regras de acesso estritas e registrar todas as alterações para facilitar a reversão. Boas servidores dividem o trabalho em tarefas menores, distribuem-as em muitos computadores e adicionam backups para que nunca percam dados. Em resumo, o Servidor MCP é o hub que garante que todos os agentes compartilhem contexto fresco, seguro e correto.

Acesse os seguintes recursos para saber mais:

- [@opensource@punkeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
- [@article@Introdução ao Servidor MCP do Azure ](https://devblogs.microsoft.com/azure-sdk/introducing-the-azure-mcp-server/)
- [@article@O Guia Último sobre MCP](https://guangzhengli.com/blog/en/model-context-protocol)
- [@article@Servidores MCP da AWS para Assistentes de Código](https://aws.amazon.com/blogs/machine-learning/introducing-aws-mcp-servers-for-code-assistants-part-1/)
