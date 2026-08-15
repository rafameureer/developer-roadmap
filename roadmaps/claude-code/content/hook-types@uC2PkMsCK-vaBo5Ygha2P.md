# Tipos de Hooks

No Claude Code, você pode configurar três tipos distintos de manipuladores para seus hooks—Comando, Prompt e Agente—dependendo se você precisa de um script, uma decisão de "chamada de julgamento" da IA ou um pesquisador especializado para validar ações. Os hooks de Comando (`type: "command"`) são scripts shell determinísticos que executam comandos padrão (como `npm run lint`) e usam códigos de saída para aprovar ou bloquear uma ação com uma mensagem de erro. Os hooks de Prompt (`type: "prompt"`) usam um modelo leve do Claude para avaliações de turnos únicos, onde o modelo analisa o contexto (por exemplo, "É essa mensagem de commit descritiva?") e retorna uma decisão simples em formato JSON sim/não. Finalmente, os hooks de Agente (`type: "agent"`) são os mais sofisticados, iniciando um subagente multi-turno com acesso a ferramentas (como `Read` ou `Grep`) para realizar verificações profundas e autônomas antes de decidir se o agente principal deve prosseguir.

Acesse os seguintes recursos para saber mais:

- [@oficial@Tipos de Hooks](https://code.claude.com/docs/en/hooks)
- [@oficial@Hooks baseados em Prompt](https://code.claude.com/docs/en/hooks-guide#prompt-based-hooks)
- [@oficial@Hooks baseados em Agente](https://code.claude.com/docs/en/hooks-guide#agent-based-hooks)
- [@oficial@Automatize fluxos de trabalho com hooks](https://code.claude.com/docs/en/hooks-guide)
