# Modelo de Segurança dos Workers

Os Cloudflare Workers operam em um ambiente seguro e isolado. O runtime dos Workers impõe limites estritos de segurança, impedindo que os Workers acessem dados sensíveis ou interfiram em outros processos. Os Workers têm acesso limitado ao mundo exterior e devem solicitar explicitamente recursos. A rede global do Cloudflare fornece proteção intrínseca contra DDoS e mitiga vulnerabilidades comuns da web. Esse ambiente de execução seguro garante que os Workers possam processar solicitações de forma segura, sem comprometer a segurança geral da plataforma.

Acesse os seguintes recursos para saber mais:

- [@official@Modelo de Segurança · Cloudflare](https://developers.cloudflare.com/workers/reference/security-model/)
- [@official@Workers RPC — Modelo de Visibilidade e Segurança - Documentação do Cloudflare](https://developers.cloudflare.com/workers/runtime-apis/rpc/visibility/)
