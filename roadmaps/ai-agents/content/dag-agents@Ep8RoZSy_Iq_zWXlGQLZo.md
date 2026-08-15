# Agentes DAG

Um agente DAG (Directed Acyclic Graph) é composto por partes pequenas chamadas de nós que formam um gráfico unidirecional sem laços. Cada nó executa uma tarefa e passa seu resultado para o próximo. Como não há ciclos, os dados sempre se movem em frente, tornando os fluxos de trabalho fáceis de seguir e depurar. Nós independentes podem ser executados em paralelo, acelerando as tarefas. Se um nó falhar, você pode rastrear e corrigir essa parte sem tocar no resto. Agentes DAG são ideais para trabalhos como limpeza de dados, raciocínio em várias etapas ou fluxos de trabalho onde não é necessário voltar atrás.

Acesse os seguintes recursos para saber mais:

- [@official@Airflow: Documentação de Grafos Direcionados Acíclicos](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html)
- [@article@O que são DAGs em sistemas AI?](https://www.restack.io/p/version-control-for-ai-answer-what-is-dag-in-ai-cat-ai)
- [@video@DAGs explicados de forma simples](https://www.youtube.com/watch?v=1Yh5S-S6wsI)
