# Programação Assíncrona no Django

A programação assíncrona permite que um programa execute várias tarefas simultaneamente, sem precisar esperar a conclusão de cada uma antes de iniciar a próxima. Em vez de bloquear e esperar, o programa pode alternar entre as tarefas conforme necessário, melhorando a eficiência. No Django, isso é alcançado usando ferramentas como as palavras-chave `async` e `await` em Python, juntamente com visualizações e middleware assíncronos, permitindo que o aplicativo manipule mais solicitações simultaneamente e reduza os tempos de resposta, especialmente para tarefas envolvendo operações de E/S como consultas de banco de dados ou chamadas a APIs externas.

Acesse os seguintes recursos para saber mais:

- [@oficial@Suporte assíncrono](https://docs.djangoproject.com/en/6.0/topics/async/)
- [@artigo@Desbloqueando o desempenho: um guia sobre suporte assíncrono no Django](https://dev.to/pragativerma18/unlocking-performance-a-guide-to-async-support-in-django-2jdj)
- [@artigo@Executando tarefas simultaneamente em visualizações assíncronas do Django](https://fly.io/django-beats/running-tasks-concurrently-in-django-asynchronous-views/)
- [@vídeo@Introdução às visualizações assíncronas no Django | async/await em visualizações do Django](https://www.youtube.com/watch?v=YneIutRhmgo)
