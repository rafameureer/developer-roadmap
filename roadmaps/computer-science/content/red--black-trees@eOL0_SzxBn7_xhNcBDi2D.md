# Árvores Vermelhas e Pretas

Na ciência da computação, uma árvore vermelha-preta é um tipo de árvore binária de busca auto-balanceada. Cada nó armazena um bit extra representando "cor", usado para garantir que a árvore permaneça balanceada durante inserções e exclusões.

Estas são traduções de uma árvore 2-3 (veja abaixo).

Na prática: As árvores vermelhas-pretas oferecem garantias piores-caso para o tempo de inserção, tempo de exclusão e tempo de busca. Isso não só as torna valiosas em aplicações sensíveis ao tempo como também em blocos de construção em outras estruturas de dados que fornecem garantias piores-caso; por exemplo, muitas estruturas de dados usadas na geometria computacional podem ser baseadas em árvores vermelhas-pretas, e o Agendador Completomente Justo usado nos núcleos Linux atuais usa árvores vermelhas-pretas. Na versão 8 do Java, a coleção HashMap foi modificada de forma que, em vez de usar uma LinkedList para armazenar elementos idênticos com códigos de hash ruins, é usada uma Árvore Vermelha e Preta.

Acesse os seguintes recursos para saber mais:

- [@artigo@Árvore Vermelha e Preta - Wikipedia](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
- [@artigo@Introdução à Busca Binária e Árvores Vermelhas e Pretas](https://www.topcoder.com/thrive/articles/An%20Introduction%20to%20Binary%20Search%20and%20Red-Black%20Trees)
- [@vídeo@Árvores Vermelhas e Pretas (playlist) em 30 minutos](https://www.youtube.com/playlist?list=PL9xmBV_5YoZNqDI8qfOZgzbqahCUmUEin)
- [@vídeo@Aduni - Algoritmos - Aula 4 (link salta para o ponto de início)](https://youtu.be/1W3x0f_RmUo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3871)
- [@vídeo@Aduni - Algoritmos - Aula 5](https://www.youtube.com/watch?v=hm2GHwyKF1o&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=5)
