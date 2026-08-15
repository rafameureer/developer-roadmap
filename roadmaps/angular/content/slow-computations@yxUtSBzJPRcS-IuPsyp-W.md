# Computações Lentas

Em cada ciclo de detecção de alteração, o Angular synchronousmente avalia todas as expressões do modelo em componentes com base na estratégia de detecção e executa os hooks de ciclo de vida `ngDoCheck`, `ngAfterContentChecked`, `ngAfterViewChecked` e `ngOnChanges`. Para remover computações lentas, você pode otimizar algoritmos, armazenar dados com pipes puros ou memoização, e limitar o uso dos hooks de ciclo de vida.

Acesse os seguintes recursos para saber mais:

- [@oficial@Computações Lentas](https://angular.dev/best-practices/slow-computations)
- [@artigo@Otimização de Desempenho do Angular](https://davembush.medium.com/angular-performance-optimization-5ec630d2b8f1)
