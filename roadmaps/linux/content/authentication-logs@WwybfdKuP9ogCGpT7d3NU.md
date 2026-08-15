# Logs de Autenticação

Logs de autenticação no Linux registram todos os eventos relacionados à autenticação, como logins, alterações de senha e comandos sudo. Localizados em `/var/log/auth.log` (Debian) ou `/var/log/secure` (RHEL/CentOS), esses logs ajudam a detectar ataques de força bruta e tentativas não autorizadas de acesso. Use `tail /var/log/auth.log` para visualizar entradas recentes. Análise regular dos logs é essencial para monitoramento de segurança do servidor.

Acesse os seguintes recursos para saber mais:

- [@artigo@Monitorando Logs de Autenticação no Linux](https://betterstack.com/community/guides/logging/monitoring-linux-auth-logs/)
- [@artigo@Como Ver o Histórico de Logins no Linux - Guia do Linux Handbook](https://linuxhandbook.com/linux-login-history/)
