# Versão / Aliases

No AWS Lambda, **Versão** fornece uma maneira de gerenciar iterações distintas e separadas de uma função Lambda, permitindo tanto a redução de riscos quanto ciclos de desenvolvimento mais eficientes. Por outro lado, um **Alias** é um ponteiro para uma versão específica da função Lambda. Aliases são mutáveis; eles podem ser reassociados a uma versão diferente, manifestando uma forma de flexibilidade. Com aliases, você pode evitar atualizações diretas dos gatilhos de eventos ou serviços downstream, pois eles podem apontar para um alias e a correspondente versão pode ser atualizada, separando assim as alterações na infraestrutura/código.

Acesse os seguintes recursos para saber mais:

- [@official@AWS Lambda Versioning](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html)
