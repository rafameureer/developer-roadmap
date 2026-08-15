# Renderização do Lado do Cliente (CSR)

Na Renderização do Lado do Cliente (CSR) com React, o navegador baixa uma página HTML mínima e o JavaScript necessário para a página. O JavaScript é então usado para atualizar o DOM e renderizar a página. Quando a aplicação é carregada pela primeira vez, o usuário pode notar um pequeno atraso antes de ver a página completa, isso ocorre porque a página não é totalmente renderizada até que todo o JavaScript seja baixado, analisado e executado.

Após a primeira carga da página, navegar para outras páginas no mesmo site geralmente é mais rápido, pois apenas os dados necessários precisam ser recuperados, e o JavaScript pode re-renderizar partes da página sem exigir um recarregamento completo da página.

Acesse os seguintes recursos para saber mais:

- [@official@Client-side Rendering (CSR)](https://nextjs.org/docs/pages/building-your-application/rendering/client-side-rendering)
- [@article@O que é Renderização do Lado do Cliente (CSR)?](https://prismic.io/blog/client-side-rendering)
