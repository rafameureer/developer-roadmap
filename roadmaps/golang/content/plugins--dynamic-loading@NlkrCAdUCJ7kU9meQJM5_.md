# Plugins & Dynamic Loading

O sistema de plugins do Go permite carregar bibliotecas compartilhadas (.so files) em tempo de execução usando o pacote `plugin`. Construído com `go build -buildmode=plugin`. Permite arquiteturas modulares, mas tem limitações: Unix-only, problemas de compatibilidade de versão e complexidade.

Acesse os seguintes recursos para saber mais:

- [@official@pacote plugin](https://pkg.go.dev/plugin)
- [@article@Plugins com Go: Como usar o pacote padrão do Go](https://medium.com/profusion-engineering/plugins-with-go-7ea1e7a280d3)
- [@article@Plugin em Golang](https://dev.to/jacktt/plugin-in-golang-4m67)
