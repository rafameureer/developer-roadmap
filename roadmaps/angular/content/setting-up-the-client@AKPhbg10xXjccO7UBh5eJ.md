# Configurando o Cliente

Antes de você poder usar `HttpClient` em seu aplicativo, deve configurá-lo usando a injeção de dependências. O `HttpClient` é fornecido usando a função auxiliar `provideHttpClient`, que a maioria dos apps inclui nas provedores do aplicativo em `app.config.ts`. Se o seu app estiver usando bootstrap baseado em NgModule, você pode incluir `provideHttpClient` nos provedores de seu `NgModule`.

Acesse os seguintes recursos para saber mais:

- [@oficial@Configurando HttpClient](https://angular.dev/guide/http/setup)
- [@vídeo@Configurando HttpClient no Angular (NgModule)](https://www.youtube.com/watch?v=hBFtim1vO3M)
