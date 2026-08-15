# Ativos Estáticos

Conteúdo estático é qualquer arquivo armazenado em um servidor e que é o mesmo toda vez que é entregue aos usuários. Exemplos desse tipo de conteúdo incluem arquivos HTML e imagens. O Next.js pode servir arquivos estáticos sob uma pasta chamada `public` no diretório raiz. Os arquivos dentro de `public` podem então ser referenciados pelo seu código a partir da URL base (`/`). É importante notar que o Next.js não pode armazenar em cache seguramente os ativos na pasta public porque eles podem mudar.

Acesse os seguintes recursos para saber mais:

- [@oficial@Pasta Public](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder)
