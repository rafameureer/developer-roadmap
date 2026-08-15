# Pontos de Acesso à API

As Rotas da API permitem que você crie um ponto de acesso à API dentro de uma aplicação Next.js. As rotas da API funcionam de maneira diferente nos Roteadores de Páginas e Roteadores de Aplicativos:

* Roteador de Páginas: Historicamente, o Next.js usava pages/api/* para APIs. Este método dependia de objetos de solicitação/resposta do Node.js e uma API semelhante ao Express.
* Roteador de Aplicativos (Padrão): Introduzido no Next.js 13, o Roteador de Aplicativos totalmente abraça as APIs padrão web Request/Response. Em vez de pages/api/*, você pode agora colocar arquivos `route.ts` ou `route.js` em qualquer lugar dentro do diretório app/.

Acesse os seguintes recursos para saber mais:

- [@official@Manipuladores de Rota e Middleware](https://nextjs.org/docs/app/getting-started/route-handlers-and-middleware)
- [@official@Rotas da API para Roteador de Páginas](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
- [@official@Construindo APIs com o Next.js](https://nextjs.org/blog/building-apis-with-nextjs)
- [@video@Tutorial do Next.js 15 - Manipuladores de Rota](https://www.youtube.com/watch?v=27Uj6BeIDV0)
