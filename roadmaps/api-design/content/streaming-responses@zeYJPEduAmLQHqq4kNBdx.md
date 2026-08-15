# Respostas em Streaming

As respostas em streaming permitem que um servidor envie dados ao cliente incrementalmente à medida que se tornam disponíveis, em vez de bufferizar toda a resposta e enviá-la de uma só vez. Isso é útil para conjuntos de dados grandes, downloads de arquivos, rastreamento de logs ou texto gerado por IA onde os primeiros tokens podem ser entregues ao usuário antes da resposta completa estar pronta. O codificação em transferência em pedaços HTTP e SSE são métodos comuns para streaming, e significativamente melhoram o desempenho percebido para respostas lentas ou grandes.

Acesse os seguintes recursos para saber mais:

- [@artigo@Streaming de Dados com APIs REST](https://apisyouwonthate.com/blog/streaming-data-with-rest-apis/)
- [@vídeo@https://www.youtube.com/watch?v=xTTtqwGWemw](https://www.youtube.com/watch?v=xTTtqwGWemw&t=210s)
