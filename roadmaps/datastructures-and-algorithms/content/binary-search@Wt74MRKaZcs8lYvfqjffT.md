# Busca Binária

A `Busca Binária` é um tipo de algoritmo de busca que segue a estratégia dividir e conquistar. Funciona em um array ordenado dividindo repetidamente o intervalo de busca ao meio. Inicialmente, o espaço de busca é todo o array e o alvo é comparado com o elemento do meio do array. Se eles não forem iguais, a metade em que o alvo não pode estar é eliminada e a busca continua na metade restante, novamente pegando o elemento do meio para comparar com o alvo, e repetindo isso até que o alvo seja encontrado. Se a busca terminar com a metade restante sendo vazia, o alvo não está no array. A Busca Binária é log(n) porque corta o espaço de busca pela metade a cada passo.

Acesse os seguintes recursos para saber mais:

- [@video@Aprenda Busca Binária em 10 minutos](https://www.youtube.com/watch?v=xrMppTpoqdw)
