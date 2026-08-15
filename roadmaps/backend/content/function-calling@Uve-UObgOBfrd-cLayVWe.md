# Chamada de Função

O "chamamento de função" nativo do LLM permite que um grande modelo linguístico decida quando executar uma parte de código e quais entradas passar para ele. Primeiro, você diz ao modelo quais funções estão disponíveis. Para cada uma delas, você fornece um nome curto, uma descrição curta e uma lista de argumentos com seus tipos. Durante uma conversa, o modelo pode responder em JSON que corresponde a este esquema em vez de texto simples. Seu programa-wrapper lê o JSON, chama a função real e depois devolve o resultado para o modelo para que ele possa continuar. Este loop ajuda um agente a pesquisar na web, procurar dados, enviar e-mails ou fazer qualquer outra tarefa que você expõe. Porque a saída é estruturada, você comete menos erros do que quando o modelo tenta escrever código bruto ou comandos em linguagem natural.

Acesse os seguintes recursos para saber mais:

- [@artigo@Guia Completo sobre Chamada de Função em LLMs](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/)
- [@artigo@Chamada de Função com LLMs | Guia de Engenharia de Prompt](https://www.promptingguide.ai/applications/function_calling)
- [@artigo@Chamada de Função com LLMs Abertos](https://medium.com/@rushing_andrei/function-calling-with-open-source-llms-594aa5b3a304)
- [@vídeo@LLM Chamada de Função - Uma Visão Profunda em Ferramentas de IA](https://www.youtube.com/watch?v=gMeTK6zzaO4)
