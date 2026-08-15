# Ciclo de Vida do Bucket

O ciclo de vida de um bucket R2 envolve a criação, o uso (armazenamento e recuperação de objetos) e eventualmente a exclusão. Você cria um bucket para abrigar seus dados. Os objetos são então carregados, acessados e gerenciados dentro do bucket. O Cloudflare não possui regras de ciclo de vida embutidas como alguns outros provedores de armazenamento, então a expiração dos objetos geralmente requer lógica personalizada via Workers. Finalmente, quando o bucket não for mais necessário e após garantir que ele esteja vazio, você pode excluí-lo.

Acesse os seguintes recursos para saber mais:

- [@oficial@Buckets · Cloudflare R2](https://developers.cloudflare.com/r2/buckets/)
- [@oficial@Ciclo de Vida do Bucket · Cloudflare R2](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/lifecycle/)
