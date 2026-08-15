# Prioridades de Processos

O Linux atribui níveis de prioridade a processos para uma utilização eficiente dos recursos e tempos de execução. Os valores de prioridade ("nice" values) variam de -20 (maior prioridade) a +19 (menor prioridade). Visualize as prioridades com `ps -eo pid,pri,user,comm`. Altere as prioridades usando `renice -5 -p [PID]`. Essencial para otimização do desempenho do sistema e gerenciamento de recursos de CPU.

Acesse os seguintes recursos para saber mais:

- [@artigo@Entendendo as Prioridades das Threads de Processos no Linux](https://blogs.oracle.com/linux/post/task-priority)
- [@artigo@Como Manipular a Prioridade dos Processos no Linux](https://www.itsmarttricks.com/how-to-manipulate-process-priority-in-linux-using-nice-and-renice-commands/)
