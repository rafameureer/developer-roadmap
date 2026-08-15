# Verificando Logs de Serviço

O Systemd captura a saída de todos os serviços gerenciados e armazena em um registro binário, chamado journal, que é gerenciado pelo journald. Você pode visualizar os logs de um serviço específico usando `journalctl -u nome-do-servico`. Úteis flags incluem `-f` para seguir os logs em tempo real, `--since` e `--until` para filtrar por intervalo de tempo e `-n` para limitar o número de linhas exibidas. Os logs incluem tanto stdout/stderr do processo quanto eventos de ciclo de vida do systemd.

Acesse os seguintes recursos para saber mais:

- [@article@Expliquei Journalctl: Como Visualizar e Analisar Logs do Systemd](https://uptimerobot.com/knowledge-hub/logging/journalctl-explained-how-to-view-and-analyze-systemd-logs/)
- [@article@Como Usar journalctl para Ver e Manipular Logs do Systemd no Linux](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs)
