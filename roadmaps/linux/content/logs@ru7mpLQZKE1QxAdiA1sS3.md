# Logs do Sistema

O Linux mantém logs que documentam atividades do sistema, erros e mensagens do kernel. Os logs de inicialização registram todas as operações durante o início do sistema para fins de solução de problemas. Use `dmesg` para visualizar mensagens do buffer de ring do kernel em tempo real ou acesse os logs em `/var/log`. O Systemd usa `journalctl` para logging. Os níveis de log variam desde emergência (sistema inutilizável) até mensagens de depuração.

Acesse os seguintes recursos para saber mais:

- [@artigo@Como usar o comando journalctl para analisar logs no Linux](https://linuxhandbook.com/journalctl-command/)
- [@artigo@Como verificar logs do sistema no Linux](https://www.fosslinux.com/8984/how-to-check-system-logs-on-linux-complete-usage-guide.htm)
- [@artigo@O que é dmesg no Linux e como eu uso?](https://linuxconfig.org/what-is-dmesg-and-how-do-i-use-it)
