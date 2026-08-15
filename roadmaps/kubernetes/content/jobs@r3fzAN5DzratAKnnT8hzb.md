# Jobs

Um Job é um controlador que gerencia a execução de uma tarefa finita ou job em lote. Os Jobs são usados para executar tarefas curtas, como processamento em lote, análise de dados ou backups, que terminam e depois encerram. Os Jobs criam um ou mais pods para executar a tarefa e monitoram o status de conclusão de cada pod. Se um pod falhar ou terminar, o Job cria automaticamente um novo pod substituto para garantir que a tarefa seja concluída com sucesso. Os Jobs são definidos por um arquivo YAML que inclui um modelo de pod, critérios de conclusão e outras configurações.

Acesse os seguintes recursos para saber mais:

- [@official@Documentação dos Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
- [@article@Como Kubernetes Está se Transformando em um Agendador Universal](https://thenewstack.io/how-kubernetes-is-transforming-into-a-universal-scheduler/)
- [@video@Tutorial | Jobs no Kubernetes](https://www.youtube.com/watch?v=j1EnBbxSz64)
