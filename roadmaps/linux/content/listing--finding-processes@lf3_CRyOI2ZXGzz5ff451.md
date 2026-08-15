# Listagem e Encontramento de Processos

Os processos do Linux podem ser monitorados usando o sistema de arquivos virtual `proc` e comandos como `ps`, `top` e `htop`. Use `ps -ef` para capturas de tela de processos, `top`/`htop` para visualizações em tempo real. O diretório `/proc` contém informações detalhadas sobre os processos. Exiba detalhes específicos de um processo com `cat /proc/{PID}/status`. Essencial para o monitoramento e solução de problemas de desempenho do sistema.

Acesse os seguintes recursos para saber mais:

- [@artigo@O Sistema de Arquivos /proc](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
- [@artigo@O que é um processo no Linux/Unix?](https://www.scaler.com/topics/linux-process/)
- [@artigo@Explorando o Sistema de Arquivos /proc do Linux](https://www.redhat.com/en/blog/linux-proc-filesystem)
