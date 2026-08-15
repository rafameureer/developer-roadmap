# Comunicação entre Workers

A comunicação entre Workers permite que diferentes Workers do Cloudflare interajam e compartilhem dados. Isso pode ser feito através de:

- **Durable Objects:** Os Workers podem compartilhar dados persistentes e coordenar o estado usando Durable Objects.
- **KV Storage:** Os Workers podem ler e escrever dados em um namespace KV compartilhado.
- **Webhooks:** Um Worker pode acionar outro enviando uma solicitação de webhook.

Estes métodos permitem que você construa aplicativos complexos onde diferentes Workers lidam com tarefas específicas e colaboram para atingir um objetivo comum.

Acesse os seguintes recursos para saber mais:

- [@oficial@Como funciona o Workers for Platforms - Docs do Cloudflare](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/how-workers-for-platforms-works/)
- [@artigo@Cooperação entre Workers do Cloudflare](https://dev.to/chimame/cooperation-between-cloudflare-workers-has-become-amazing-thanks-to-rpc-support-4co9)
