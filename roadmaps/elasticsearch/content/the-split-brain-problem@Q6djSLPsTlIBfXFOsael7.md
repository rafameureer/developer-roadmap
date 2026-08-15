# O Problema "Split Brain"

O problema "split brain" ocorre em sistemas distribuídos quando um cluster de nós se divide em duas ou mais sub-clusters independentes que não conseguem se comunicar entre si. Cada sub-cluster pode então acreditar que é o cluster principal e começar a tomar decisões independentes, potencialmente levando a inconsistências de dados e conflitos conforme cada sub-cluster opera como se fosse a única autoridade. Essa situação pode resultar em perda ou corrupção de dados quando as partições eventualmente reúnem-se.

Acesse os seguintes recursos para saber mais:

- [@oficial@Decisão baseada em quórum](https://www.elastic.co/docs/deploy-manage/distributed-architecture/discovery-cluster-formation/modules-discovery-quorums)
- [@artigo@Evitando o problema de split brain no Elasticsearch e como recuperar](https://bigdataboutique.com/blog/avoiding-the-elasticsearch-split-brain-problem-and-how-to-recover-f6451c)
- [@artigo@Split-Brain em Sistemas Distribuídos](https://dzone.com/articles/split-brain-in-distributed-systems)
