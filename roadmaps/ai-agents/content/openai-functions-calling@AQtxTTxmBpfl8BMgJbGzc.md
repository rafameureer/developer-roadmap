# Chamada de Funções do OpenAI

O Chamamento de Funções do OpenAI permite que você forneça a um modelo linguístico uma lista de ferramentas e o deixe decidir qual usar e com quais dados. Você descreve cada ferramenta com um nome curto, o que ela faz e a forma de seus inputs em um pequeno esquema JSON-like. Em seguida, você passa a mensagem do usuário e esta lista de ferramentas para o modelo. Em vez de texto normal, o modelo pode responder com um bloco JSON que nomeia a ferramenta e preenche os argumentos necessários. Seu programa lê este bloco, executa a função real e pode enviar o resultado de volta para a próxima etapa. Este padrão torna as ações dos agentes claras, fáceis de analisar e difíceis de abusar, porque o modelo não pode executar código por conta própria e todas as chamadas passam por suas verificações. Também reduz o uso de hacks de prompt e formatos incorretos, então os agentes funcionam mais rápido e com segurança.

Acesse os seguintes recursos para saber mais:

- [@official@Documentação oficial do OpenAI – Chamada de Funções](https://platform.openai.com/docs/guides/function-calling)
- [@official@Guia do Cozinho do OpenAI – Usando Funções com Modelos GPT](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_with_chat_models.ipynb)
- [@article@@officialOpenAI Blog – Anúncio de Chamada de Funções e Outras Atualizações](https://openai.com/blog/function-calling-and-other-api-updates)
- [@article@@officialOpenAI API Reference – Seção de Funções](https://platform.openai.com/docs/api-reference/chat/create#functions)
- [@article@@officialOpenAI Community – Discussões e Exemplos sobre Chamada de Funções](https://community.openai.com/tag/function-calling)
