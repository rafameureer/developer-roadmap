# Poluição de Zona

`Zone.js` é um mecanismo de sinalização que o Angular usa para detectar quando o estado da aplicação pode ter mudado. Em alguns casos, tarefas agendadas ou microtarefas não fazem nenhuma alteração no modelo de dados, o que torna a detecção de mudança desnecessária. Exemplos comuns são `requestAnimationFrame`, `setTimeout` e `setInterval`. Você pode identificar a detecção de mudança com Angular DevTools e executar código fora da zona do Angular para evitar chamadas desnecessárias de detecção de mudança.

Acesse os seguintes recursos para saber mais:

- [@official@Poluição de Zona](https://angular.dev/best-practices/zone-pollution)
- [@official@Angular DevTools](https://angular.dev/tools/devtools)
- [@video@NgZone em Angular - Melhore o desempenho executando código fora do Angular](https://www.youtube.com/watch?v=7duYY9IFIuw)
- [@video@4 Otimizações de Desempenho em Tempo Real](https://www.youtube.com/watch?v=f8sA-i6gkGQ)
