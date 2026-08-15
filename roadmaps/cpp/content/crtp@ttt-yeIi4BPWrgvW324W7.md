# CRTP

O Padrão de Template Recorrente Curioso (CRTP) é um idiom em C++ onde uma classe template herda de sua própria especialização. Esta técnica atinge a polimorfismo estático, oferecendo uma alternativa ao polimorfismo em tempo de execução usando funções virtuais. O CRTP permite a personalização do comportamento da classe base sem o overhead de chamadas de função virtual, habilitando o polimorfismo em tempo de compilação para melhorar o desempenho. É útil quando você precisa estender ou modificar a funcionalidade nas classes derivadas enquanto mantém a eficiência evitando o custo de tempo de execução associado às funções virtuais.

Acesse os seguintes recursos para saber mais:

- [@article@CRTP (Curiously Recurring Template Pattern) em C++](https://medium.com/@sagar.necindia/crtp-curiously-recurring-template-pattern-in-c-90981941bf38)
- [@video@Tutorial de C++: Como usar CRTP para acelerar seu código](https://www.youtube.com/watch?v=Srx4eiBdpdQ)
