# Arquitetura de Isolados

A arquitetura isolada do Cloudflare para os Workers depende de isolados leves do V8. Cada Worker roda em seu próprio isolado, fornecendo uma forte isolamento dos outros Workers e da infraestrutura subjacente. Os isolados iniciam rapidamente e consomem recursos mínimos, permitindo escalonamento rápido. Essa arquitetura impede que o código de um Worker afete os outros, melhorando a segurança e a estabilidade. A isolação garante que, mesmo se um Worker contiver vulnerabilidades, ele não possa comprometer toda a rede do Cloudflare ou as aplicações dos outros clientes.

Acesse os seguintes recursos para saber mais:

- [@official@Referências Arquiteturas · Referência de Arquitetura do Cloudflare](https://developers.cloudflare.com/reference-architecture/)
- [@official@Arquitetura de Segurança do Cloudflare](https://developers.cloudflare.com/reference-architecture/architectures/security/)
