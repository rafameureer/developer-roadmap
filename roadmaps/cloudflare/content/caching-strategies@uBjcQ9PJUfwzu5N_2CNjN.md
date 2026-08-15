# Estratégias de Cache

Os Workers do Cloudflare permitem um controle fino sobre o cache. Você pode usar a API de Cache para armazenar e recuperar respostas diretamente dentro do seu Worker, evitando o servidor de origem. As estratégias incluem:

- **Cache-First:** Serve da cache se disponível, caso contrário, fetch do origin.
- **Network-First:** Sempre fetch do origin, cacheando a resposta para solicitações subsequentes.
- **Stale-While-Revalidate:** Serve da cache imediatamente, então atualiza a cache em segundo plano.

Você também pode manipular os cabeçalhos de cache HTTP (Cache-Control, Expires) para controlar como o CDN do Cloudflare armazena conteúdo. A eficácia no cache é crucial para melhorar o desempenho e reduzir a carga no servidor de origem.

Acesse os seguintes recursos para saber mais:

- [@oficial@Cache · Workers do Cloudflare](https://developers.cloudflare.com/workers/runtime-apis/cache/)
- [@oficial@Como funciona o Cache · Workers do Cloudflare ](https://developers.cloudflare.com/workers/reference/how-the-cache-works/)
