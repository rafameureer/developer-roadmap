# Chunking

O passo de chunking na Geração Complementada por Recuperação (RAG) envolve quebrar grandes documentos ou fontes de dados em partes menores e gerenciáveis. Isso é feito para garantir que o recuperador possa eficientemente pesquisar grandes volumes de dados, mantendo-se dentro dos limites de token ou de entrada do modelo. Cada chunk, geralmente um parágrafo ou seção, é convertido em uma incorporação e essas incorporações são armazenadas em um banco de dados vetorial. Quando uma consulta é feita, o recuperador procura os chunks mais relevantes em vez do documento inteiro, permitindo uma recuperação mais rápida e precisa.

Acesse os seguintes recursos para saber mais:

- [@artigo@Entendendo LangChain's RecursiveCharacterTextSplitter](https://dev.to/eteimz/understanding-langchains-recursivecharactertextsplitter-2846)
- [@artigo@Estratégias de chunking para aplicações LLM](https://www.pinecone.io/learn/chunking-strategies/)
- [@artigo@Guia de estratégias de chunking para Geração Complementada por Recuperação](https://zilliz.com/learn/guide-to-chunking-strategies-for-rag)
