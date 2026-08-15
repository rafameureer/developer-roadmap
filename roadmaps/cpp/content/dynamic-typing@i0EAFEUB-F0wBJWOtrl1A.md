# Tipagem Dinâmica

Embora o C++ seja fundamentalmente um idioma tipado estáticamente, onde os tipos de dados são verificados em tempo de compilação, ele fornece mecanismos para alcançar uma certa grau de tipagem dinâmica. Isso envolve determinar os tipos de variáveis em tempo de execução, principalmente através do uso de ponteiros `void*`, que podem apontar para qualquer tipo de dados (requerendo casting explícito), e a classe `std::any` (introduzida no C++17), um contêiner tipado seguro capaz de armazenar valores de qualquer tipo. Ambos os métodos permitem flexibilidade, mas requerem consideração cuidadosa devido ao potencial overhead em tempo de execução e erros relacionados a tipos.

Acesse os seguintes recursos para saber mais:

- [@artigo@Tipagem Dinâmica no C++](https://codesignal.com/learn/courses/advanced-functional-programming-techniques/lessons/dynamic-type-declaration-in-cpp)
- [@vídeo@Tipagem Estática vs Tipagem Dinâmica](https://www.youtube.com/watch?v=GqXpFycPWLE)
