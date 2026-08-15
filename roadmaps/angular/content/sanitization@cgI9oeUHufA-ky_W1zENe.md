# Sanitização

A sanitização é a inspeção de um valor não confiável, transformando-o em um valor seguro para inserir no DOM. Em muitos casos, a sanitização não altera o valor em nada algum. A sanitização depende do contexto: Um valor que é inofensivo em CSS pode ser potencialmente perigoso em uma URL.

O Angular sanitiza valores não confiáveis para HTML e URLs. A sanitização de URLs de recursos não é possível porque elas contêm código arbitrário. No modo de desenvolvimento, o Angular imprime um aviso no console quando precisa alterar um valor durante a sanitização.

Acesse os seguintes recursos para saber mais:

- [@oficial@Sanitização e Contextos de Segurança](https://angular.dev/best-practices/security#sanitization-and-security-contexts)
