# Parar

O gatilho `Stop` é um evento de ciclo de vida final que é acionado quando o Claude Code acredita que já terminou toda sua resposta e está prestes a retornar o controle para o usuário. Diferentemente do `PostToolUse`, que dispara após cada edição de arquivo ou comando individual, o gatilho `Stop` só roda uma vez no final da interação "turn".

Acesse os seguintes recursos para saber mais:

- [@official@Referência de Gatilhos](https://code.claude.com/docs/en/hooks)
- [@official@Automatize fluxos de trabalho com gatilhos](https://code.claude.com/docs/en/hooks-guide)
