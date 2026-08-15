# Configuração do Modelo

O Claude Code oferece uma hierarquia de configuração de modelo altamente flexível que permite equilibrar velocidade, custo e profundidade de raciocínio em diferentes tarefas. Você pode trocar modelos instantaneamente durante uma sessão ativa usando o comando `/model`, especificar um modelo no início com a bandeira `--model` ou definir um padrão default permanente em seu arquivo `~/.claude/settings.json` usando a chave `model`. O sistema suporta aliases semânticos como sonnet (padrão para codificação diária), haiku (rápido e eficiente) e opus (alto raciocínio para arquiteturas complexas), bem como um modo especializado `opusplan` que usa inteligentemente o Opus para planejamento estratégico antes de automaticamente trocar para Sonnet para a implementação do código real. Além disso, você pode ajustar desempenho em modelos suportados ajustando o `effortLevel` (baixo, médio ou alto), que controla quanto "tempo de pensamento" o Claude aloca para resolver puzzles lógicos difíceis em vez de gerar respostas rápidas.

Acesse os seguintes recursos para saber mais:

- [@oficial@Configuração do modelo](https://code.claude.com/docs/en/model-config#model-configuration)
- [@artigo@Guia completo sobre a configuração do modelo no Claude Code](https://www.eesel.ai/blog/model-configuration-claude-code)
