# HEAD

O arquivo `HEAD` é o coração de como o Git sabe a SHA-1 da última confirmação quando executa comandos como `git branch <branch>`. Ele atua como uma referência simbólica, apontando para a ramificação atual. No entanto, em casos raros, HEAD pode conter o valor SHA-1 real de um objeto Git, como ao verificar out uma tag, confirmação ou ramificação remota, o que coloca seu repositório em um estado "HEAD desanexado".

Acesse os seguintes recursos para saber mais:

- [@oficial@Git Internals - Git References - The HEAD](https://git-scm.com/book/pt-br/v2/Git-Internais-Git-References#:~:text=want%20to%20create.-,The%20HEAD,-The%20question%20now)
- [@vídeo@Aprenda os Conceitos Essenciais do Git: HEAD e Detached HEAD](https://www.youtube.com/watch?v=HvDjbAa9ZsY)
