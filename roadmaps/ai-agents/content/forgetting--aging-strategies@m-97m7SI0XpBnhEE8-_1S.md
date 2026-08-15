# Estratégias de Esquecimento / Idade

Estratégias de esquecimento ou idade ajudam um agente de IA a manter apenas as partes úteis da sua memória e descartar o resto ao longo do tempo. O agente pode marcar cada memória com uma marca temporal e reduzir sua importância à medida que ela envelhece, ou pode remover itens que não foram usados há algum tempo, como uma lista "menos recentemente usado". Alguns sistemas atribuem a cada memória uma pontuação de relevância; quando o espaço se esgota, eles excluem os itens com a pontuação mais baixa primeiro. Outros mantêm uma janela deslizante fixa dos eventos mais recentes ou criam resumos curtos e armazenam esses em vez de detalhes brutos. Esses métodos impedem que o armazenamento de memória cresça sem limites, reduzem custos de armazenamento e permitem que o agente se concentre em metas atuais. Escolher a combinação certa de regras de idade é um equilíbrio: esquecer demais e o agente perde contexto, esquecer demais e ele desperdiça recursos ou responde a fatos obsoletos.

Acesse os seguintes recursos para saber mais:

- [@artigo@Gerenciamento de Memória](https://python.langchain.com/docs/how_to/chatbots_memory/)
- [@artigo@Gerenciamento de Memória para Agentes de IA](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/memory-management-for-ai-agents/4406359)
