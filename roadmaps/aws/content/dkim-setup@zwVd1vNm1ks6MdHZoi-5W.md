# Configuração de DKIM

DKIM (DomainKeys Identified Mail) é um padrão que previne o spoofing de e-mail. Ele permite que uma organização assuma a responsabilidade por transmitir uma mensagem de uma maneira que possa ser verificada por provedores de caixa postal. Essa verificação é possível através da autenticação criptográfica. No Amazon SES, você pode configurar DKIM adicionando um conjunto de três registros CNAME à configuração DNS do seu domínio de envio. Cada registro mapeia um subdomínio fictício de seu domínio de envio para um domínio mantido pelo Amazon SES. Depois que adicionar esses registros e eles propagarem pela infraestrutura de DNS da Internet, você pode começar a enviar e-mail autenticado do seu domínio.

Acesse os seguintes recursos para saber mais:

- [@oficial@DKIM](https://dkim.org/)
- [@artigo@DKIM - Cloudflare](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)
