# Escopo

O escopo de vida é um tipo de injeção de dependência que cria uma nova instância de um objeto para cada solicitação única, mas reutiliza a mesma instância para a mesma solicitação. Isso significa que se vários componentes dentro da mesma solicitação dependerem do mesmo serviço, todos receberão a mesma instância. No entanto, se outra solicitação for feita, uma nova instância do serviço será criada para essa solicitação.

O escopo de vida é útil quando você tem serviços específicos para uma determinada solicitação, como um contexto de banco de dados com escopo de solicitação. Isso permite que você tenha uma instância separada e isolada do serviço para cada solicitação única, o que pode ajudar a prevenir a contaminação cruzada de dados entre solicitações e melhorar o desempenho.

Acesse os seguintes recursos para saber mais:

- [@artigo@Injeção de Dependência - O que é Escopo?](https://javaranch.com/journal/2008/10/dependency-injection-what-is-scope.html)
- [@artigo@Escopo Efetivo da Injeção de Dependência](https://medium.com/android-news/effective-dependency-injection-scoping-4bac813d4491)
