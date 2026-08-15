# Tratamento Básico de Erros

Go usa o tratamento explícito de erros com valores de retorno de erro. As funções retornam um erro como último valor. Verifique o padrão `if err != nil`. Crie erros usando `errors.New()` ou `fmt.Errorf()`. Sem exceções - os erros são valores a serem manipulados explicitamente.

Acesse os seguintes recursos para saber mais:

- [@official@Tratamento de Erros e Go](https://go.dev/blog/error-handling-and-go)
- [@article@Dominando o Tratamento de Erros em Go: Um Guia Completo](https://medium.com/hprog99/mastering-error-handling-in-go-a-comprehensive-guide-fac34079833f)
- [@article@Erros e Manipulação de Exceções em Golang](https://golangdocs.com/errors-exception-handling-in-golang)
