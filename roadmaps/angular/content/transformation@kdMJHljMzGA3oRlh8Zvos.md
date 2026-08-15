# Transformação

No RxJS, "transformação" refere-se ao processo de modificar ou manipular os dados emitidos por um Observable. Há uma variedade de métodos disponíveis no RxJS que podem ser usados para transformar os dados emitidos por um Observable, incluindo:

*   **map**: aplica uma função a cada item emitido pelo Observable e emite o valor resultante
*   **mergeMap**: aplica uma função a cada item emitido pelo Observable, e então mescla os Observables resultantes em um único Observable
*   **switchMap**: aplica uma função a cada item emitido pelo Observable, e então troca para o último Observable resultante
*   **concatMap**: aplica uma função a cada item emitido pelo Observable, e então concatena os Observables resultantes em um único Observable
*   **exhaustMap**: aplica uma função a cada item emitido pelo Observable, mas ignora as emissões subsequentes até que o atual Observable complete

Acesse os seguintes recursos para saber mais:

- [@oficial@A Biblioteca RxJS](https://v17.angular.io/guide/rx-library)
- [@oficial@Merge](https://www.learnrxjs.io/learn-rxjs/operators/combination/merge)
- [@oficial@Concat](https://www.learnrxjs.io/learn-rxjs/operators/combination/concat)
- [@oficial@Zip](https://www.learnrxjs.io/learn-rxjs/operators/combination/zip)
- [@oficial@switchMap](https://www.learnrxjs.io/learn-rxjs/operators/transformation/switchmap)
- [@oficial@concatMap](https://www.learnrxjs.io/learn-rxjs/operators/transformation/concatMap)
- [@oficial@exhaustMap](https://www.learnrxjs.io/learn-rxjs/operators/transformation/exhaustMap)
- [@vídeo@Prática guia de switchMap vs mergeMap vs concatMap vs exhaustMap](https://youtu.be/40pC5wHowWw)
