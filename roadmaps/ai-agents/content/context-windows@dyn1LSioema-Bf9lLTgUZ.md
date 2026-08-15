# Janelas de Contexto

Janela de contexto é o trecho de texto que um grande modelo linguístico pode ler por vez. É medido em tokens, que são partes de palavras. Se um modelo tiver uma janela de contexto de 4.000 tokens, ele só "pode olhar" até cerca de 3.000 palavras antes de ter que esquecer ou encurtar as partes mais antigas. Novos tokens empurram os antigos, como uma janela deslizante se movendo sobre o texto. O tamanho da janela estabelece limites duradouros em quanto um prompt, histórico de chat ou documento pode ser longo. Uma pequena janela força você a manter as entradas curtas ou dividir elas, enquanto uma grande janela permite que o modelo siga histórias mais longas e mantenha mais fatos. Escolher o tamanho certo da janela equilibra custo, velocidade e quantia de detalhes que o modelo pode lembrar simultaneamente.

Novas técnicas, como a geração com suporte à recuperação (RAG) e transformadores de contexto longo (ex: Claude 3, Gemini 1.5), visam estender o contexto utilitário sem atingir os limites diretamente do modelo.

Acesse os seguintes recursos para saber mais:

- [@article@O que é uma Janela de Contexto em IA?](https://www.ibm.com/think/topics/context-window)
- [@article@Escalação de Modelos Linguísticos com Geração Com Suporte à Recuperação (RAG)](https://arxiv.org/abs/2005.11401)
- [@article@Contexto Longo em Modelos Linguísticos - Família Claude 3 da Anthropic](https://www.anthropic.com/news/claude-3-family)
