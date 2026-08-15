# Workflow do Claude

O workflow do Claude Code opera como um loop agente contínuo onde a IA passa por quatro fases principais: Explorar, Planejar, Implementar e Verificar. Ele começa indexando seu código local e lendo instruções persistentes do arquivo [CLAUDE.md](http://CLAUDE.md) para se alinhar com os padrões específicos do seu projeto. Quando você emite um prompt, o Claude usa sua suíte de ferramentas internas para pesquisar os arquivos (Explorar), propor uma estratégia detalhada e passo a passo para a mudança (Planejar) e—após seu consentimento—executa as modificações usando ferramentas de edição de arquivo e shell (Implementar). O ciclo termina executando suas suites de testes definidas ou linters (Verificar) para garantir que nenhuma regressão tenha sido introduzida, frequentemente utilizando servidores MCP para sincronizar os resultados finais com plataformas externas como GitHub ou Jira.

Acesse os seguintes recursos para saber mais:

- [@official@Como funciona o Claude Code](https://code.claude.com/docs/en/how-claude-code-works)
- [@official@Fluxos de trabalho comuns](https://code.claude.com/docs/en/common-workflows)
- [@article@Meu melhor fluxo de trabalho para trabalhar com o Claude Code : r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1m3pol4/my_best_workflow_for_working_with_claude_code/)
- [@video@Fluxos de trabalho do Claude Code que aumentarão sua produtividade em 10x](https://www.youtube.com/watch?v=yZvDo_n12ns)
- [@video@O maior fluxo de trabalho do Claude Code (10x mais rápido)](https://www.youtube.com/watch?v=WdD6uD_kupY)
