# Autenticação Baseada em Sessão na Design de APIs

As Interfaces de Programação de Aplicativos (APIs) são cruciais para a construção de aplicativos de software. Entre várias considerações importantes durante a design de API, uma delas é decidir como implementar autenticação e segurança. A Autenticação Baseada em Sessão é um método popular para aplicar segurança na design de APIs.

Este método envolve o servidor criando uma sessão para o usuário após que ele faça login com sucesso, associando-a a um identificador de sessão. Este ID da Sessão é então armazenado no cliente dentro de um cookie. Em solicitações subsequentes, o servidor valida o ID da Sessão antes de processar a chamada à API. O servidor destruirá a sessão após que o usuário fizer logout, tornando assim o ID da Sessão inválido.

Entender a Autenticação Baseada em Sessão é crucial para a design de APIs seguras, especialmente em cenários onde a segurança é uma prioridade ou em sistemas legados onde este método é prevalente.

Acesse os seguintes recursos para saber mais:

- [@roadmap@Autenticação Baseada em Sessão](https://roadmap.sh/guides/session-based-authentication)
- [@artigo@Autenticação por Sessão vs Autenticação por Token](https://www.authgear.com/post/session-vs-token-authentication)
- [@vídeo@Autenticação Baseada em Sessão - Roadmap.sh](https://www.youtube.com/watch?v=gKkBEOq_shs)
