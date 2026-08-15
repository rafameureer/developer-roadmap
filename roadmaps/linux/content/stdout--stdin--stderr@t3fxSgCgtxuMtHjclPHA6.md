# Saída padrão, Entrada padrão e Erro padrão

Os processos do Linux usam três fluxos de dados padrão: STDIN (entrada), STDOUT (saída) e STDERR (mensagens de erro). STDOUT lida com a saída normal dos comandos enquanto STDERR lida especificamente com mensagens de erro. Você pode redirecionar esses fluxos usando operadores como `>` para stdout e `2>` para stderr, permitindo o tratamento separado da saída normal e dos erros para melhor script e depuração.

Acesse os seguintes recursos para saber mais:

- [@artigo@Fundamentos do Linux - Entrada/Saída, Fluxos Padrão e Redirecionamento](https://www.putorius.net/linux-io-file-descriptors-and-redirection.html)
- [@artigo@Entendendo 'stdin', 'stdout' e 'stderr' no Linux](https://www.slingacademy.com/article/understanding-stdin-stdout-and-stderr-in-linux/)
- [@artigo@Trabalhando com fluxos de dados na linha de comando do Linux](https://opensource.com/article/18/10/linux-data-streams)
