# Ambiente de Execução dos Trabalhadores

O ambiente de execução dos Trabalhadores é um ambiente de execução JavaScript leve que roda na rede da borda da Cloudflare. Está baseado no V8, o mesmo motor que impulsiona o Chrome e o Node.js, mas otimizado para velocidade e segurança. Os Trabalhadores têm acesso limitado a variáveis globais e APIs em comparação com um ambiente de Node.js tradicional, focando na manipulação de solicitações HTTP e respostas. Ele fornece APIs para caching, armazenamento KV e acesso à informação da solicitação, permitindo funções serverless performáticas e distribuídas globalmente.

Acesse os seguintes recursos para saber mais:

- [@oficial@Como funcionam os Trabalhadores · Cloudflare](https://developers.cloudflare.com/workers/reference/how-workers-works/)
- [@oficial@Introduzindo workerd: o Runtime dos Trabalhadores Aberto Fonte](https://blog.cloudflare.com/workerd-open-source-workers-runtime/)
