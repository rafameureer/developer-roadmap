# Serviço de Fundo Nativo

Um Serviço de Fundo Nativo no [ASP.NET](http://ASP.NET) é um tipo de serviço que pode ser executado em segundo plano em um dispositivo, sem a necessidade de uma sessão de usuário ativa. Esses serviços são tipicamente usados para tarefas que precisam ser executadas continuamente, como enviar notificações, pesquisar por atualizações ou processar dados.

No [ASP.NET](http://ASP.NET), um Serviço de Fundo Nativo pode ser implementado usando a interface IHostedService, que faz parte do namespace Microsoft.Extensions.Hosting. Essa interface permite criar um serviço em segundo plano que pode ser executado continuamente, mesmo quando a aplicação principal não estiver em execução.

Acesse os seguintes recursos para saber mais:

- [@artigo@Tarefas de fundo com serviços hospedados no ASP.NET](https://learn.microsoft.com/pt-br/aspnet/core/fundamentals/host/hosted-services?view=aspnetcore-7.0&tabs=visual-studio)
- [@artigo@BackgroundService no ASP.NET Core](https://medium.com/@daniel.sagita/backgroundservice-para-trabalhos-de-longa-execução-3debe8f8d25b)
- [@vídeo@Tutorial sobre Tarefas de Fundo no ASP.NET](https://youtube.com/watch?v=rugxQIH_p3A)
