# Pools de Trabalhadores

Padrão de concorrência que usa um número fixo de goroutines para processar tarefas de uma fila compartilhada. Controla o uso de recursos enquanto mantém a paralelismo. Geralmente implementado com canais bufferizados para distribuição de tarefas e WaitGroups para sincronização. Ideal para tarefas baseadas em CPU e limitação de taxa.

Acesse os seguintes recursos para saber mais:

- [@article@GO: Como Escrever um Pool de Trabalhadores](https://dev.to/justlorain/go-how-to-write-a-worker-pool-1h3b)
- [@article@Concorrência Eficiente em Go: Uma Profundidade na Implementação do Pattern de Pool de Trabalhadores](https://rksurwase.medium.com/efficient-concurrency-in-go-a-deep-dive-into-the-worker-pool-pattern-for-batch-processing-73cac5a5bdca)
