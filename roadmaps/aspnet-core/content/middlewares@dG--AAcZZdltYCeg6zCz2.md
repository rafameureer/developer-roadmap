# Middlewares

Middleware é software que se encontra entre um sistema operacional e o software de aplicação, facilitando a comunicação e a troca de dados entre eles. No contexto do desenvolvimento web, middleware refere-se a componentes de software que lidam com solicitações e respostas em uma aplicação web. Esses componentes são tipicamente executados em um pipeline, com cada componente realizando uma tarefa específica, como autenticação, registro ou roteamento.

No framework [ASP.NET](http://ASP.NET) Core, middleware é um conceito chave usado para construir aplicativos web. Componentes de middleware são adicionados ao pipeline da aplicação usando a interface `IApplicationBuilder`, e são executados na ordem em que são adicionados. Por exemplo, uma aplicação pode ter componentes de middleware para lidar com autenticação, registro e roteamento, nesta ordem.

Acesse os seguintes recursos para saber mais:

- [@artigo@O que é Middleware?](https://www.redhat.com/en/topics/middleware/what-is-middleware)
- [@artigo@Introdução ao Middleware](https://www.techtarget.com/searchapparchitecture/definition/middleware)
- [@artigo@O que é Middleware em .NET?](https://www.talend.com/resources/what-is-middleware/)
