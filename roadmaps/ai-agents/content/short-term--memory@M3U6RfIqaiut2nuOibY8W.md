# Memória de Curto Prazo

A memória de curto prazo são fatos que são passados como parte da solicitação para o LLM, por exemplo. Pode haver uma solicitação como a seguir:

    Perfil do Usuário:
    - nome: {nome}
    - idade: {idade}
    - especialidade: {especialidade}
    
    O usuário está atualmente aprendendo sobre {tópico_atual}. O usuário tem alguns objetivos em mente que são:
    - {objetivo_1}
    - {objetivo_2}
    - {objetivo_3}
    
    Ajude o usuário a atingir os objetivos.
    

Observe como injetamos o perfil do usuário, tópico atual e objetivos na solicitação. Todos esses são fatos de memória de curto prazo.

Acesse os seguintes recursos para saber mais:

- [@artigo@Gerenciamento de Memória em Agentes AI](https://python.langchain.com/docs/how_to/chatbots_memory/)
- [@artigo@Construindo Agentes AI Inteligentes: Gerenciando Memória de Curto e Longo Prazo](https://redis.io/blog/build-smarter-ai-agents-manage-short-term-and-long-term-memory-with-redis/)
- [@artigo@Armazenando e Recuperando Conhecimento para Agentes](https://www.pinecone.io/learn/langchain-retrieval-augmentation/)
- [@artigo@Memória de Curto Prazo vs Memória de Longo Prazo em Agentes AI](https://adasci.org/short-term-vs-long-term-memory-in-ai-agents/)
- [@vídeo@Construindo uma Memória Semelhante ao Cérebro para Agentes AI](https://www.youtube.com/watch?v=VKPngyO0iKg)
