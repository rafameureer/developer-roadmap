# volatile

O qualificador `volatile` instrui o compilador a que um valor de uma variável pode mudar inesperadamente, fora do fluxo normal do programa, como através de registradores de hardware ou manipuladores de sinal. Isso previne o compilador de aplicar otimizações que assumem que o valor da variável permanece o mesmo entre leituras. É comum em programação embarcada e código de nível baixo que interage diretamente com o hardware.

Acesse os seguintes recursos para saber mais:

- [@article@“O que realmente `volatile` faz — e não faz” — em C](https://medium.com/@wongjushao/what-volatile-really-does-and-doesnt-do-in-c-7a98e9e135c3)
- [@video@Como usar a palavra-chave `volatile` em C?](https://www.youtube.com/watch?v=6tIWFEzzx9I)
