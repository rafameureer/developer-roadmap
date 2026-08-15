# Síncrono vs Assíncrono em APIs

Quando projetar APIs, uma decisão crítica é decidir se criar uma API síncrona ou assíncrona. As APIs síncronas são aquelas que mantêm uma conexão aberta e esperam por uma resposta antes de prosseguir, portanto, operando em sequência. Isso pode levar a codificação eficiente e simples de entender, mas pode causar problemas de desempenho ao lidar com tarefas longas, pois o chamador tem que esperar até que o processo termine.

Por outro lado, as APIs assíncronas não esperam por uma resposta antes de prosseguir para a próxima tarefa, permitindo que várias operações sejam executadas simultaneamente. Isso pode resultar em melhor desempenho e resposta especialmente em aplicativos que precisam lidar com múltiplas solicitações simultaneamente. No entanto, codificar para APIs assíncronas pode ser complexo devido a problemas como condições de corrida e callbacks. Entender as diferenças entre esses dois tipos de design de API é crucial para criar APIs eficientes e eficazes.

Acesse os seguintes recursos para saber mais:

- [@artigo@APIs Assíncronas — Tudo o Que Você Precisa Saber](https://blog.hubspot.com/website/asynchronous-api)
- [@artigo@As Diferenças entre APIs Síncronas e Assíncronas](https://nordicapis.com/the-differences-between-synchronous-and-asynchronous-apis/)
- [@artigo@Compreendendo APIs Assíncronas](https://blog.postman.com/understanding-asynchronous-apis/)
