# Palavra-chave Volatile

A palavra-chave `volatile` em Java é um modificador que pode ser aplicado a variáveis de instância. Ela garante que todas as threads vejam o valor mais atual da variável. Sem `volatile`, cada thread pode cachear sua própria cópia da variável, levando a inconsistências quando múltiplas threads acessam e modificam-a simultaneamente. Usar `volatile` força a thread a ler o valor da variável diretamente da memória principal e escrever as alterações diretamente de volta à memória principal, evitando o cache local da thread.

Acesse os seguintes recursos para saber mais:

- [@artigo@Java Volatile Keyword](https://jenkov.com/tutorials/java-concurrency/volatile.html)
- [@artigo@Guia sobre a Palavra-chave Volatile em Java](https://www.baeldung.com/java-volatile)
