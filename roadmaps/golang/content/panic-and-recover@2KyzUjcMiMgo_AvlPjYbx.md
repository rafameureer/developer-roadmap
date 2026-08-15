# Pânico e Recuperação

A função `panic()` para a execução e desfaz a pilha, enquanto a função `recover()` captura pânicos em funções diferidas. Use com moderação para erros irrecoveráveis. Embora o Go enfatize erros explícitos, panic/recover servem como uma rede de segurança para situações excepcionais.

Acesse os seguintes recursos para saber mais:

- [@oficial@Defer, Panic e Recuperação](https://go.dev/blog/defer-panic-and-recover)
- [@artigo@Lidando com Pânicos em Go](https://www.digitalocean.com/community/tutorials/handling-panics-in-go)
