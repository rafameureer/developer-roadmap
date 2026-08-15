# Non-tail recursion

A recursão de cauda é quando uma função pode retornar diretamente o resultado de uma chamada recursiva - não há operações pendentes e não há necessidade de preservar a estrutura do quadro da pilha. Então, ela pode ser traduzida para um "goto com argumentos", e o uso da pilha será constante.

Na "non-tail recursion", há operações pendentes após a chamada recursiva, e o quadro da pilha não pode ser removido.

Acesse os seguintes recursos para saber mais:

- [@article@O que é non-tail recursion?](https://www.quora.com/What-is-non-tail-recursion)
- [@article@Tail vs Non-Tail Recursion](https://www.baeldung.com/cs/tail-vs-non-tail-recursion)
- [@video@Recursão (Problema Resolvido 1)](https://www.youtube.com/watch?v=IVLUGb_gDDE)
- [@video@Tipos de Recursão (Parte 2) | Tail & Non-tail Recursion](https://www.youtube.com/watch?v=HIt_GPuD7wk)
- [@feed@Explore os melhores posts sobre Recursão](https://app.daily.dev/tags/recursion?ref=roadmapsh)
