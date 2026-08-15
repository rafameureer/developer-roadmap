# Schedulers
 
Schedulers no RxSwift controlam em qual thread ou fila a trabalho dos Observables é executado. MainScheduler executa o trabalho na thread principal para atualizações de UI, enquanto ConcurrentDispatchQueueScheduler e SerialDispatchQueueScheduler executam o trabalho nas filas de fundo. Os operadores observeOn e subscribeOn especificam respectivamente quais schedulers lidam com a observação e a assinatura.

Acesse os seguintes recursos para saber mais:

- [@official@Documentação Scheduler ReactiveX](https://reactivex.io/documentation/scheduler.html)
- [@opensource@Documentação Scheduler RxSwift](https://github.com/ReactiveX/RxSwift/blob/main/Documentation/Schedulers.md)
- [@article@Schedulers no RxSwift](https://docs.rxswift.org/rxswift/schedulers)
