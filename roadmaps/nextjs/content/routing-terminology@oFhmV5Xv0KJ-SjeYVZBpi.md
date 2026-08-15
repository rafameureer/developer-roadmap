# Terminologia de Roteamento em Next.js

Em Next.js, o roteamento é principalmente gerenciado através do diretório `app` (introduzido no Next.js 13) e do antigo diretório `pages`. Termos-chave incluem:

*   **Rota:** Um caminho de URL específico que se mapeia para um componente ou página particular. Por exemplo, `/blog/my-first-post`.

*   **Segmento de Rota:** Uma parte do caminho da URL. Em `/blog/my-first-post`, `blog` e `my-first-post` são segmentos de rota.

*   **Roteamento Baseado em Sistema de Arquivos:** O Next.js usa um roteador baseado em sistema de arquivos. A estrutura dos seus diretórios e arquivos dentro do diretório `app` ou `pages` define diretamente as rotas da sua aplicação.

*   **Rotas Dinâmicas:** Rotas que incluem parâmetros, permitindo criar páginas com base em dados. Por exemplo, `/blog/[slug]`, onde `[slug]` é um parâmetro dinâmico.

*   **Rota Índice:** A rota que é servida quando um usuário visita um diretório. Geralmente representada por um arquivo `index.js` ou `page.js` dentro de um diretório.

*   **Layout:** Um componente que envolve várias páginas, fornecendo uma estrutura UI consistente (como cabeçalhos e rodapés) em diferentes rotas.

*   **Componente Link:** O componente `<Link>` do `next/link` é usado para navegação entre rotas no lado do cliente, oferecendo melhor desempenho que as tags tradicionais `<a>`.

Acesse os seguintes recursos para saber mais:

- [@oficial@Estrutura e organização do projeto](https://nextjs.org/docs/app/getting-started/project-structure)
- [@vídeo@Tutorial Next.js 15 - Roteamento](https://www.youtube.com/watch?v=9602Yzvd7i)
- [@vídeo@Tutorial Next.js 15 - Rotas Aninhadas](https://www.youtube.com/watch?v=H7JjKjkC33c)
- [@vídeo@Tutorial Next.js 15 - Rotas Dinâmicas](https://www.youtube.com/watch?v=k9g6aVLH3p4)
- [@vídeo@Tutorial Next.js 15 - Rotas Aninhadas Dinâmicas](https://www.youtube.com/watch?v=edrJf0GKfAI)
