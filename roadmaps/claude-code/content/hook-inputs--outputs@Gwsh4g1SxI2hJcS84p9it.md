# Entradas e Saídas de Hook

Os Hooks se comunicam por meio de uma interface JSON padrão: as entradas são passadas para o hook via `stdin`, e as saídas são retornadas via `stdout` para influenciar a próxima ação do agente. O payload de entrada geralmente inclui um objeto `contexto` contendo metadados da sessão e dados específicos do evento, como o nome da `ferramenta` e seus argumentos (por exemplo, o código exato sendo escrito ou o comando sendo executado). Para responder, seu hook deve retornar um objeto JSON.

Acesse os seguintes recursos para saber mais:

- [@official@Entradas e Saídas de Hook](https://code.claude.com/docs/en/hooks#hook-input-and-output)
