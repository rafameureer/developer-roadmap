# Representação de Grafos

Um grafo pode ser representado como uma matriz de adjacência ou uma lista de adjacência.

A matriz de adjacência é um array bidimensional de tamanho `V x V` onde `V` é o número de vértices em um grafo. Considere que o array bidimensional seja `adj[][]`, uma posição `adj[i][j] = 1` indica que há uma aresta do vértice `i` ao vértice `j`.

A lista de adjacência é um array de vetores. O tamanho do array é igual ao número de vértices. Considere que o array seja `array[]`. Uma entrada `array[i]` representa a lista de vértices adjacentes ao vértice i-ésimo. Esta representação também pode ser usada para representar um grafo pesado. Os pesos das arestas podem ser representados como listas de pares.

Acesse os seguintes recursos para saber mais:

- [@article@Matriz de Adjacência - Representação de Grafo](https://www.programiz.com/dsa/graph-adjacency-matrix)
- [@article@Lista de Adjacência - Representação de Grafo](https://www.programiz.com/dsa/graph-adjacency-list)
