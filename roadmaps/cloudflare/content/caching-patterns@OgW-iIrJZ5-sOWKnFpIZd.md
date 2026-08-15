# Modelos de Caching

O caching é um aspecto crucial na construção de aplicativos performáticos e escaláveis. Os Workers da Cloudflare oferecem vários modelos de caching que você pode usar para otimizar o desempenho do seu aplicativo. Esses padrões incluem:

- **Cache-First:** Servir a partir do cache se disponível, caso contrário, buscar da origem.
- **Network-First:** Sempre buscar da origem, armazenando a resposta no cache para solicitações subsequentes.
- **Stale-While-Revalidate:** Servir imediatamente a partir do cache, depois atualizar o cache em segundo plano.

Você também pode manipular os cabeçalhos de cache HTTP (Cache-Control, Expires) para controlar como o CDN da Cloudflare armazena conteúdo. O caching eficaz é crucial para melhorar o desempenho e reduzir a carga no servidor de origem.

Acesse os seguintes recursos para saber mais:

- [@oficial@Como funciona o Cache · Workers KV](https://developers.cloudflare.com/workers/reference/how-the-cache-works/)
- [@artigo@Estratégias de Caching](https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/caching-patterns.html)
- [@artigo@Caching Estático e Dinâmico](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)
