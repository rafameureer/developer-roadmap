# Padrões de Middleware

Os padrões de middleware em Cloudflare Workers permitem encadear funções para processar solicitações ou respostas de uma maneira modular. Cada função de middleware executa uma tarefa específica (por exemplo, autenticação, registro, modificação de cabeçalhos) antes de passar a solicitação/resposta para a próxima função na cadeia. Isso promove a reutilização do código, a separação dos assuntos e facilita a manutenção. Com a composição de middleware, você pode construir pipelines complexos de processamento de solicitações.

Acesse os seguintes recursos para saber mais:

- [@oficial@Middleware · Cloudflare Pages](https://developers.cloudflare.com/pages/functions/middleware/)
- [@artigo@Uma Arquitetura de Middleware para Cloudflare Workers](https://boxesplusarrows.com/blog/a-middleware-architecture-for-cloudflare-workers/)
