# Agente RAG

O Agente RAG (Retrieval-Augmented Generation) mistura a busca com a geração de linguagem para que possa responder perguntas usando fatos frescos e confiáveis. Quando um usuário envia uma consulta, o agente primeiro transforma essa consulta em uma embedding — basicamente uma lista de números que capturam seu significado. Em seguida, ele procura por embeddings similares em um banco de dados vetorial que armazena passagens de páginas da web, PDFs ou outros textos. As melhores correspondências retornam como contexto. O agente coloca a pergunta original e essas passagens em um grande modelo de linguagem. O modelo escreve a resposta final, ancorando cada frase no texto recuperado. Esta configuração mantém o modelo menor, reduz errados suposições e permite que o sistema atualize seu conhecimento apenas adicionando novos documentos ao banco de dados. Ferramentas comuns para construir um agente RAG incluem um modelo de embedding, um armazenamento vetorial como FAISS ou Pinecone, e um LLM conectado por meio de um framework como LangChain ou LlamaIndex.

Acesse os seguintes recursos para saber mais:

- [@artigo@O que é o RAG? - Inteligência Artificial de Geração Aumentada por Recuperação](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [@artigo@O Que é a Geração Aumentada por Recuperação, ou RAG?](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
