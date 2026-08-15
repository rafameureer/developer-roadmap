# Ciclo de Vida dos Trabalhadores

O ciclo de vida de um Trabalhador da Cloudflare é curto e sem estado. Cada invocação começa quando uma solicitação atinge a borda da rede da Cloudflare. O Trabalhador executa seu código para lidar com a solicitação. Uma vez que a resposta é enviada (ou ocorre um erro), a instância do Trabalhador termina. Não há estado persistente entre as solicitações, a menos que você use serviços como KV ou Objetos Duráveis. Esta natureza sem estado garante escalabilidade e tempos de resposta rápidos. Compreender este ciclo de vida é crucial para projetar Trabalhadores eficientes que possam lidar com altos volumes de solicitações.

Acesse os seguintes recursos para saber mais:

- [@oficial@RPC dos Trabalhadores - Ciclo de Vida](https://developers.cloudflare.com/workers/runtime-apis/rpc/lifecycle/)
- [@oficial@Como funcionam os Trabalhadores · Cloudflare](https://developers.cloudflare.com/workers/reference/how-workers-works/)
- [@oficial@Introduzindo workerd: o Runtime dos Trabalhadores Aberto Fonte](https://blog.cloudflare.com/workerd-open-source-workers-runtime/)
