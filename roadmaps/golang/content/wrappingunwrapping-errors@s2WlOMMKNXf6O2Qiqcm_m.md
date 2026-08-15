# Wrapping/Unwrapping Errors

Crie cadeias de erros preservando os erros originais ao adicionar contexto usando `fmt.Errorf()` com o verbo `%w`. Use `errors.Unwrap()`, `errors.Is()` e `errors.As()` para trabalhar com erros embrulhados. Permite contextos de erro ricos para facilitar a depuração.

Acesse os seguintes recursos para saber mais:

- [@article@Golang: embrulhamento / desembrulhamento de erros](https://medium.com/@vajahatkareem/golang-error-wrapping-multierror-759d04bdbfaf)
- [@article@Embrulhamento de Erros em Go - Exemplo de Tratamento de Erros em Go](https://go-cookbook.com/snippets/error-handling/error-wrapping)
