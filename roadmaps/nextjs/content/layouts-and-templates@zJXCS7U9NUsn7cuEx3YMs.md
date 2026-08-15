# Layouts e Templates

Os layouts e templates oferecem uma maneira de compartilhar elementos da interface do usuário em várias páginas, mantendo o estado e evitando re-renderizações desnecessárias. Os layouts envolvem as páginas, persistindo entre alterações de rota para preservar coisas como barras de navegação ou barras laterais.

Os templates são semelhantes aos layouts em que envolvem cada layout filho ou página. Diferentemente dos layouts que persistem entre rotas e mantêm o estado, os templates criam uma nova instância para cada um de seus filhos na navegação. Isso significa que quando um usuário navega entre rotas que compartilham um template, uma nova instância do componente é montada, os elementos DOM são recriados, o estado não é preservado e os efeitos são sincronizados novamente.

Acesse os seguintes recursos para saber mais:

- [@oficial@Layouts para App Router](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layouts)
- [@oficial@Layouts para Pages Router](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)
- [@oficial@Templates para App Router](https://nextjs.org/docs/app/api-reference/file-conventions/template)
- [@artigo@Um guia sobre layouts e layouts aninhados no Next.js](https://blog.logrocket.com/guide-next-js-layouts-nested-layouts/)
- [@vídeo@Tutorial do Next.js 15 - Layouts](https://www.youtube.com/watch?v=NK-8a8EzWrU)
- [@vídeo@Tutorial do Next.js 15 - Templates](https://www.youtube.com/watch?v=yfww2kplO-k)
