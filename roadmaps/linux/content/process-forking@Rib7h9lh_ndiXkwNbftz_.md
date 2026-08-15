# Forkagem de Processos

A forkagem de processos usa a chamada de sistema `fork()` para criar processos filhos a partir de processos-pai, permitindo a execução concorrente. Os processos-filho são quase cópias perfeitas dos pais com diferentes PIDs. Mudanças nos processos-filho não afetam os pais. Essencial para entender a criação e o controle de processos no Linux em ambientes multi-processo.

Acesse os seguintes recursos para saber mais:

- [@artigo@fork — Manual do Linux](https://www.man7.org/linux/man-pages/man2/fork.2.html)
- [@artigo@Entendendo a Chamada de Sistema fork() no Linux](https://thelinuxcode.com/fork-system-call-linux/)
- [@artigo@Chamadas de sistema Linux: Criando processos usando fork](https://medium.com/@joshuaudayagiri/linux-process-calls-creating-process-using-fork-52a1eac7de8b)
