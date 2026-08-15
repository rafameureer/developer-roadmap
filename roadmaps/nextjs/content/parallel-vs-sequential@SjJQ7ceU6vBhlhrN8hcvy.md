# Paralelo vs Sequencial

Quando você está buscando dados dentro de componentes React, é necessário estar ciente de dois padrões de busca de dados: Paralelo e Sequencial.

Com a busca de dados sequencial, as solicitações em uma rota dependem umas das outras e, portanto, criam cascadas. Pode haver casos onde você deseja esse padrão porque uma busca depende do resultado da outra ou você deseja que uma condição seja satisfeita antes da próxima busca para economizar recursos. No entanto, esse comportamento também pode ser inconsciente e levar a tempos de carregamento mais longos.

Com a busca de dados paralela, as solicitações em uma rota são iniciadas com entusiasmo e carregarão os dados ao mesmo tempo. Isso reduz as cascadas cliente-servidor e o tempo total para carregar os dados.

Acesse os seguintes recursos para saber mais:

- [@oficial@Busca de dados paralela e sequencial](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#parallel-and-sequential-data-fetching)
