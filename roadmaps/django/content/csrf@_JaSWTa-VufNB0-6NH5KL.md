# CSRF

CSRF (Cross-Site Request Forgery) é uma vulnerabilidade de segurança da web onde um site malicioso engana o navegador do usuário para realizar ações em um site confiável sem o conhecimento do usuário. No Django forms, a proteção contra CSRF funciona incluindo um token único e secreto em cada formulário. Quando o formulário é enviado, o Django verifica se esse token corresponde ao armazenado na sessão do usuário. Se eles não correspondem, a solicitação é rejeitada, impedindo que o atacante forgeie solicitações.

Acesse os seguintes recursos para saber mais:

- [@official@Proteção contra Cross Site Request Forgery](https://docs.djangoproject.com/pt-br/6.0/ref/csrf/)
- [@official@Como usar a proteção CSRF do Django](https://docs.djangoproject.com/pt-br/6.0/howto/csrf/)
- [@article@Guia de Proteção CSRF no Django: Exemplos e Como Habilitar](https://www.stackhawk.com/blog/django-csrf-protection-guide/)
- [@video@O que é Token CSRF no Django e Por Que Ele É Usado?](https://www.youtube.com/watch?v=iJmezMBJqEs)
- [@video@Django - Solicitações AJAX, HTMX & Tokens CSRF](https://www.youtube.com/watch?v=lc1sOvRaFpg)
