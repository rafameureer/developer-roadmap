# Invalidações

As `Invalidações` no AWS CloudFront é um conceito onde você remove arquivos (objetos) do cache do CloudFront antes de atingir o período de expiração. O AWS CloudFront, como qualquer outro CDN, armazena cópias dos seus arquivos estáticos em seu cache até que atinja sua duração TTL (tempo de vida). Mas em algumas situações, você pode querer remover ou substituir esses arquivos. Por exemplo, esses podem ser alterações em arquivos CSS ou JS. É nesse momento que as Invalidações entram em cena. Com isso, você pode remover imediatamente objetos ou arquivos de locais de borda.

Acesse os seguintes recursos para saber mais:

- [@official@Invalidações Cloudfront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html)
