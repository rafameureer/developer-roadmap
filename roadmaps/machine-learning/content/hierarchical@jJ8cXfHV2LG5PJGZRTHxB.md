# Agrupamento Hierárquico

O agrupamento hierárquico é um método de agrupar pontos de dados em clusters com base na sua similaridade, construindo uma hierarquia de clusters. Ele começa tratando cada ponto de dados como seu próprio cluster e então mescla iterativamente os clusters mais próximos até que apenas um cluster reste ou seja atingido um critério de parada. Esse processo cria uma estrutura árvore-like chamada dendrograma, que representa visualmente a hierarquia dos clusters. O scikit-learn fornece uma implementação do agrupamento hierárquico aglomerativo através da classe `AgglomerativeClustering`, que permite especificar o critério de ligação (por exemplo, ward, complete, average) para determinar como a distância entre os clusters é calculada.

Acesse os seguintes recursos para saber mais:

- [@artigo@Agrupamento Hierárquico | scikit-learn](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)
- [@artigo@O que é Agrupamento Hierárquico?](https://www.ibm.com/think/topics/hierarchical-clustering)
