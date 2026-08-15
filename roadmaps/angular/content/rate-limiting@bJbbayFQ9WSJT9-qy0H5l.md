# Limitação de taxa

A limitação de taxa no RxJS refere-se à prática de restringir a taxa em que eventos ou dados podem ser emitidos por um observável. Isso pode ser útil em situações onde a taxa de entrada de dados é maior do que a taxa em que ela pode ser processada, ou quando há limites na quantidade de solicitações que podem ser feitas a um servidor. Existem alguns operadores diferentes no RxJS que podem ser usados para limitação de taxa, como throttleTime e sampleTime. Esses operadores podem ser usados para limitar a taxa de emissões de um observável descartando as emissões que ocorrem com frequência demais. Outro operador é auditTime, ele emite o último valor do Observable-fonte durante janelas de tempo periódicas.

Acesse os seguintes recursos para saber mais:

- [@artigo@throttleTime](https://www.learnrxjs.io/learn-rxjs/operators/filtering/throttletime)
- [@artigo@auditTime](https://www.learnrxjs.io/learn-rxjs/operators/filtering/audittime)
- [@artigo@Blog e Tutoriais sobre RxJS](https://blog.angular-university.io/functional-reactive-programming-for-angular-2-developers-rxjs-and-observables/)
