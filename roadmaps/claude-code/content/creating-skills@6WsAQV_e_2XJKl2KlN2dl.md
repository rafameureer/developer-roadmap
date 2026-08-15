# Criando Habilidades Personalizadas

Para criar uma habilidade personalizada no Claude Code, você deve estabelecer uma nova pasta dentro do diretório `.claude/skills/` contendo um arquivo `SKILL.md` que defina a identidade e a lógica da habilidade. Esse arquivo começa com um bloco de frontmatter YAML contendo um nome único `name` e uma descrição detalhada `description`, que o Claude usa como gatilho para "saber" quando ativar a habilidade, e pode incluir uma bandeira opcional `disable-model-invocation: true` se você quiser que a habilidade seja executada como um fluxo de trabalho manual e determinístico em vez de autônomo.

Acesse os seguintes recursos para saber mais:

- [@curso@Habilidades de Agente com Anthropic](https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/)
- [@oficial@Estenda o Claude com habilidades](https://code.claude.com/docs/en/skills#extend-claude-with-skills)
- [@oficial@Como criar habilidades personalizadas](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [@artigo@Construindo Sua Primeira Habilidade de Agente Claude Code: Um Sistema Simples de Memória de Projeto que Salva Horas](https://pub.spillwave.com/build-your-first-claude-code-skill-a-simple-project-memory-system-that-saves-hours-1d13f21aff9e)
- [@vídeo@Habilidades do Claude Code & skills.sh - Crash Course](https://www.youtube.com/watch?v=rcRS8-7OgBo)
