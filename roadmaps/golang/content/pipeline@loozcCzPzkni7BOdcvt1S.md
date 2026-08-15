# Pipeline

O padrão de concorrência encadeia etapas de processamento onde a saída de uma etapa se torna a entrada da próxima. Cada etapa é executada simultaneamente usando goroutines e canais, permitindo o processamento em paralelo e a separação de preocupações. Comum em processamento de dados, fluxos de transformação e aplicações de streaming.

Acesse os seguintes recursos para saber mais:

- [@official@Concorrência Pipelines](https://go.dev/blog/pipelines)
- [@article@Padrão Pipeline em Go: Um Guia Prático](https://dev.to/leapcell/pipeline-pattern-in-go-a-practical-guide-5dmm)
- [@article@Aplicando Padrões de Concorrência Modernos em Fluxos de Dados](https://medium.com/amboss/applying-modern-go-concurrency-patterns-to-data-pipelines-b3b5327908d4)
