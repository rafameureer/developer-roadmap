# Pollagem Curta

Na pollagem curta, o cliente solicita informações ao servidor. O servidor processa a solicitação. Se dados estiverem disponíveis para a solicitação, o servidor responde à solicitação com as informações necessárias. No entanto, se o servidor não tiver dados disponíveis para o cliente, ele retorna uma resposta vazia. Em ambas as situações, a conexão será fechada após retornar a resposta. Os clientes continuam emitindo novas solicitações mesmo depois que o servidor envia respostas vazias. Este mecanismo aumenta o custo de rede no servidor.

Visite os seguintes recursos para saber mais:

- [@artigo@O que são Long-Polling, Websockets, Server-Sent Events (SSE) e Comet?](https://stackoverflow.com/questions/11077857/what-are-long-polling-websockets-server-sent-events-sse-and-comet)
