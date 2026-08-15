# Dois Montículos

O método de dois montículos usa um montículo máximo para armazenar a metade inferior dos números e um montículo mínimo para armazenar a metade superior. Esse setup permite acessar rapidamente o maior valor da metade inferior e o menor valor da metade superior em tempo constante. Inserções e deleções têm complexidade logarítmica, e os montículos são balanceados para que o mediano possa ser encontrado em O(1) tempo. Esse abordagem é especialmente útil para manter dinamicamente o mediano de uma sequência de dados longa ou em fluxo, onde repetirmente ordenar os dados seria ineficiente (O(n log n) por ordenação).

Acesse os seguintes recursos para saber mais:

- [@artigo@Dois Montículos — Um Padrão de Codificação para a Encontrada do Mediano (Emre Bolat)](https://emre.me/coding-patterns/two-heaps/)
- [@vídeo@Padrão de Codificação - Dois Montículos](https://www.youtube.com/watch?v=9P7W5aEaatQ)
