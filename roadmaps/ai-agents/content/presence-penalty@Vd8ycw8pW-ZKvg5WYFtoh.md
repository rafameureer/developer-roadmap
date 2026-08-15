# Penalidade de Presença

A penalidade de presença é uma configuração que você pode ajustar quando pedir a um grande modelo linguístico escrever. Ela empurra o modelo para escolher palavras que ainda não usou. Cada vez que uma palavra já apareceu, o modelo recebe uma pequena redução no score por escolhê-la novamente. Uma penalidade mais alta dá cortes maiores, então o modelo procura por novas palavras e ideias frescas. Uma penalidade menor permite que o modelo reutilize as palavras com mais frequência, o que pode ajudar com repetições como rimas ou listas de pontos. Ajustar esse controle ajuda você a orientar a saída para uma variedade maior ou maior consistência.

Acesse os seguintes recursos para saber mais:

- [@artigo@Entendendo Penalidade de Presença e Penalidade de Frequência](https://medium.com/@pushparajgenai2025/understanding-presence-penalty-and-frequency-penalty-in-openai-chat-completion-api-calls-2e3a22547b48)
- [@artigo@Diferença entre Penalidade de Frequência e Penalidade de Presença?](https://community.openai.com/t/difference-between-frequency-and-presence-penalties/2777)
- [@artigo@Parâmetros LLM Explicados: Um Guia Prático com Exemplos](https://learnprompting.org/blog/llm-parameters)
