# Agrupamento Sobreposto

O agrupamento sobreposto permite que os pontos de dados pertençam a múltiplos grupos simultaneamente. Diferentemente do agrupamento "hard" tradicional, onde cada ponto é atribuído a apenas um grupo, o agrupamento sobreposto reconhece que os pontos de dados podem exibir características de vários grupos. Isso é particularmente útil ao lidar com conjuntos de dados complexos em que as fronteiras entre os grupos não estão bem definidas. Um algoritmo que implementa agrupamento sobreposto é o _Fuzzy C-Means (FCM)_. O FCM atribui um grau de pertencimento a cada ponto de dados para cada grupo, representando a probabilidade de pertencer a esse grupo. Um ponto de dados pode ter graus de pertencimento não-zero para múltiplos grupos, indicando sua pertencência parcial em cada.

Acesse os seguintes recursos para saber mais:

- [@artigo@Agrupamento Não Supervisionado: Uma Guia](https://builtin.com/articles/unsupervised-clustering)
