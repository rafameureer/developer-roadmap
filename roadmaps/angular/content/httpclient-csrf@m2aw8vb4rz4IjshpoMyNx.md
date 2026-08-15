# HttpClient CSRF

O HttpClient inclui um mecanismo embutido para prevenir ataques de XSRF. Quando fazendo solicitações HTTP, um interceptor lê um token de um cookie (nome padrão: XSRF-TOKEN) e o define como um cabeçalho HTTP (X-XSRF-TOKEN). Como apenas código em execução no seu domínio pode ler este cookie, o backend pode verificar que a solicitação HTTP origina-se da sua aplicação cliente e não de um atacante.

No entanto, o HttpClient só lida com a parte do lado do cliente da proteção contra XSRF. Seu serviço de backend deve ser configurado para definir o cookie para sua página e verificar que o cabeçalho esteja presente em todas as solicitações relevantes. Sem esta configuração de backend, a proteção XSRF padrão do Angular não será eficaz.

Acesse os seguintes recursos para saber mais:

- [@official@Segurança do Angular](https://angular.dev/best-practices/security#httpclient-xsrf-csrf-security)
- [@article@Como você pode proteger uma aplicação web Angular contra ataques de falsificação de solicitação cruzada?](https://www.linkedin.com/advice/3/how-can-you-protect-angular-web-app-from-cross-site-pyqwc)
- [@article@Falsificação de Solicitação Cruzada: Proteção XSRF em Angular](https://borstch.com/blog/development/cross-site-request-forgery-xsrf-protection-in-angular)
