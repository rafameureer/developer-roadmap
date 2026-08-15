# Carregamento Eager de Módulos

Por padrão, os NgModules são carregados com entusiasmo. Isso significa que assim que o aplicativo é carregado, todos os NgModules também são carregados, independentemente de serem necessários imediatamente ou não. Para aplicativos grandes com muitas rotas, considere o carregamento atrasado — um padrão de design que carrega NgModules conforme necessário. O carregamento atrasado ajuda a manter os tamanhos iniciais dos pacotes menores, o que por sua vez ajuda a diminuir os tempos de carregamento.

Acesse os seguintes recursos para saber mais:

- [@oficial@Carregamento Atrasado](https://angular.dev/guide/ngmodules/lazy-loading)
- [@artigo@Carregamento Atrasado do Angular](https://www.bairesdev.com/blog/angular-lazy-loading/)
- [@vídeo@Carregamento Atrasado no Angular: Melhorando o desempenho e a experiência do usuário](https://www.youtube.com/watch?v=mjhi27YfV8Y)
