# Pesquisa Baseada em IA

Você pode construir uma pesquisa baseada em IA usando Cloudflare Workers, Workers AI e Vectorize.

1. **Incorporar Dados:** Use Workers AI para criar embeddings vetoriais de seus dados (ex: texto, imagens).
2. **Armazenar Embeddings:** Armazene esses embeddings no Vectorize.
3. **Pesquisar:** Quando um usuário pesquisa, crie o embedding da consulta usando Workers AI e, em seguida, use o Vectorize para encontrar os embeddings mais semelhantes em seu banco de dados.
4. **Retornar Resultados:** Retorne os itens de dados correspondentes como resultados de pesquisa.

Acesse os seguintes recursos para saber mais:

- [@oficial@Cloudflare + AI](https://ai.cloudflare.com/)
- [@oficial@Agentes da Cloudflare](https://developers.cloudflare.com/agents/)
- [@artigo@Como usar Workers AI da Cloudflare para construir uma Pesquisa Baseada em IA](https://dev.to/charlestehio/how-to-use-cloudflare-workers-ai-for-building-an-ai-powered-search-bar-51jn)
