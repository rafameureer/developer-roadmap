# Processamento de Mensagens

Com as Filas do Cloudflare, o processamento de mensagens envolve enviar mensagens para uma fila por um produtor (geralmente um Worker) e depois consumir essas mensagens da fila por um consumidor (outro Worker ou serviço). O consumidor processa cada mensagem, realizando tarefas como transformação de dados, chamada de APIs ou atualização de bancos de dados. As Filas garantem a entrega pelo menos uma vez, o que significa que uma mensagem será entregue a um consumidor pelo menos uma vez, mesmo em caso de falhas. Os consumidores podem confirmar o processamento bem-sucedido para remover as mensagens da fila.

Acesse os seguintes recursos para saber mais:

- [@oficial@Filas do Cloudflare · Filas do Cloudflare](https://developers.cloudflare.com/queues/)
- [@oficial@Como Funcionam as Filas?](https://developers.cloudflare.com/queues/reference/how-queues-works/)
- [@artigo@Diferença entre Processamento de Fluxo e Processamento de Mensagens](https://stackoverflow.com/questions/41744506/difference-between-stream-processing-and-message-processing)
