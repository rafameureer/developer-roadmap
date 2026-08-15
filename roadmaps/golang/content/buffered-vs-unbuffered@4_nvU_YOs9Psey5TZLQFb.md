# Buffered vs Unbuffered

Canais não bufferizados fornecem comunicação síncrona - o remetente bloqueia até que o receptor esteja pronto. Canais bufferizados permitem comunicação assíncrona até a capacidade. Não bufferizados para coordenação/sequenciamento, bufferizados para desempenho/desacoplamento. Distinção crítica para o design de sistemas concorrentes.

Acesse os seguintes recursos para saber mais:

- [@artigo@Dicas avançadas sobre canais em Go](https://medium.com/@aditimishra_541/advanced-insights-into-go-channels-unbuffered-and-buffered-channels-d76d705bcc24)
- [@artigo@Canais bufferizados vs não bufferizados em GoLang](https://dev.to/akshitzatakia/buffered-vs-unbuffered-channels-in-golang-a-developers-guide-to-concurrency-3m75)
