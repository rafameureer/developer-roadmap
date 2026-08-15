# Comportamento Indefinido

Comportamento indefinido refere-se a código cujo resultado o padrão C não impõe nenhuma restrição, o que significa que um compilador pode produzir qualquer resultado, incluindo saída aparentemente correta, uma falha de crash ou uma corrupção suave que só aparece sob certas condições. As causas comuns incluem estouro de inteiro assinado, leitura de memória não inicializada, acesso a arrays fora dos limites e desreferenciamento de ponteiros inválidos. Porque o comportamento indefinido pode parecer funcionar corretamente durante os testes e falhar mais tarde ou em um compilador diferente, é uma das fontes mais importantes de bugs difíceis de diagnosticar em C.

Acesse os seguintes recursos para saber mais:

- [@article@Comportamento Indefinido](https://en.cppreference.com/c/language/behavior)
- [@article@Comportamento Indefinido em C e C++](https://dev.to/pauljlucas/undefined-behavior-in-c-and-c-3a20)
- [@video@Comportamento Indefinido em C e por que você deve saber sobre ele](https://www.youtube.com/watch?v=va_UZwTVR5g)
