# Detecção de Conflitos de Conta

Ferramenta interna para detectar conflitos de conta em programas concorrentes. Ativada com a bandeira `-race` durante a construção/teste/execução. Detecta acesso não sincronizado a variáveis compartilhadas por várias goroutines. Sobrecarga de desempenho no modo de detecção de conflito. Essencial para depurar a segurança do código concorrente.

Acesse os seguintes recursos para saber mais:

- [@oficial@Detecção de Conflitos de Conta](https://go.dev/doc/articles/race_detector)
- [@artigo@Go: Detecção de Conflitos de Conta com ThreadSanitizer](https://medium.com/a-journey-with-go/go-race-detector-with-threadsanitizer-8e497f9e42db)
- [@artigo@Detecção de Conflitos de Dados e Padrões de Conflito de Dados em Golang](https://www.sobyte.net/post/2022-06/go-data-race/)
