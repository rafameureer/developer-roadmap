# Algoritmos de Agendamento

O agendamento do CPU é o processo de selecionar um processo da fila pronta e atribuir o CPU a ele. A seleção de um processo é baseada em um algoritmo de agendamento específico. O algoritmo de agendamento é escolhido dependendo do tipo de sistema e das exigências dos processos.

Aqui está a lista de alguns dos algoritmos de agendamento mais comumente usados:

*   **First Come First Serve (FCFS):** O processo que chega primeiro é atribuído o CPU primeiro. É um algoritmo não preemptivo.
*   **Shortest Job First (SJF):** O processo com o menor tempo de execução é atribuído o CPU primeiro. É um algoritmo não preemptivo.
*   **Shortest Remaining Time First (SRTF):** O processo com o menor tempo de execução restante é atribuído o CPU primeiro. É um algoritmo preemptivo.
*   **Round Robin (RR):** O processo é atribuído o CPU por um intervalo de tempo fixo. O intervalo de tempo geralmente é 10 milissegundos. É um algoritmo preemptivo.
*   **Agendamento por Prioridade:** O processo com a maior prioridade é atribuído o CPU primeiro. É um algoritmo preemptivo.
*   **Agendamento em Níveis de Fila:** Os processos são divididos em diferentes filas com base na sua prioridade. O processo com a maior prioridade é atribuído o CPU primeiro. É um algoritmo preemptivo.
*   **Agendamento em Filas de Feedback Multinível:** Os processos são divididos em diferentes filas com base na sua prioridade. O processo com a maior prioridade é atribuído o CPU primeiro. Se um processo for preemptado, ele é movido para a próxima fila. É um algoritmo preemptivo.
*   **Highest Response Ratio Next (HRRN):** O CPU é atribuído ao próximo processo que tem a maior taxa de resposta e não ao processo com menos tempo de burto. É um algoritmo não preemptivo.
*   **Agendamento por Loteria:** O processo é atribuído o CPU com base em um sistema de loteria. É um algoritmo preemptivo.

Acesse os seguintes recursos para saber mais:

- [@article@Agendamento do CPU no Sistema Operacional](https://www.scaler.com/topics/operating-system/cpu-scheduling/)
