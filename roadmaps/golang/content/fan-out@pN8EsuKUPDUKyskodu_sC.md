# Distribuição de Fio

Padrão de concorrência que distribui trabalho de uma única fonte para múltiplos trabalhadores. Geralmente usa um canal de entrada alimentando várias goroutines. Cada trabalhador processa itens independentemente. Útil para paralelizar tarefas intensivas em CPU e aumentar a taxa de transferência através do processamento em paralelo.

Acesse os seguintes recursos para saber mais:

- [@artigo@Distribuição de Fio e Retorno de Fio: Um Padrão de Concorrência Explorado](https://www.golinuxcloud.com/go-fan-out-fan-in/)
- [@artigo@Padrões de Concorrência em Go: Distribuição de Fio, Retorno de Fio](https://medium.com/geekculture/golang-concurrency-patterns-fan-in-fan-out-1ee43c6830c4)
