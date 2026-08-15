# PreToolUse

O `PreToolUse` é uma barreira de validação que executa imediatamente após Claude decidir usar uma ferramenta (como escrever um arquivo ou executar um comando shell), mas antes que essa ferramenta realmente seja executada. Ele é principalmente usado para segurança, aplicação de políticas e sanitização de entrada, agindo como uma verificação final para garantir que a ação proposta pela IA seja segura e correta.

Acesse os seguintes recursos para saber mais:

- [@official@Referência de Hooks](https://code.claude.com/docs/en/hooks)
- [@official@Automatize fluxos de trabalho com hooks](https://code.claude.com/docs/en/hooks-guide)
- [@article@Segure suas habilidades do Claude com hooks personalizados PreToolUse](https://egghead.io/secure-your-claude-skills-with-custom-pre-tool-use-hooks~dhqko)
