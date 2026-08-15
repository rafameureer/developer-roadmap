# Git Worktrees

Usar Git worktrees com Claude Code é uma técnica de escala poderosa que permite executar várias sessões AI independentes em paralelo, sem a sobrecarga do contexto de troca ou o risco de colisão de edição de arquivos. Este fluxo de trabalho é altamente eficiente para "fan-out" tarefas: você pode supervisionar vários worktrees separados simultaneamente, aproveitando o cache de prompts para um contexto compartilhado do código-fonte e simplesmente excluindo a pasta do worktree uma vez que a branch for mesclada para manter seu ambiente limpo.

Acesse os seguintes recursos para saber mais:

- [@official@Executar sessões paralelas do Claude Code com Git worktrees](https://code.claude.com/docs/en/worktrees)
- [@article@Usando Git Worktrees para Desenvolvimento Paralelo de IA](https://stevekinney.com/courses/ai-development/git-worktrees)
- [@video@Git Worktrees: O segredo da receita do Claude Code!](https://www.youtube.com/watch?v=up91rbPEdVc)
