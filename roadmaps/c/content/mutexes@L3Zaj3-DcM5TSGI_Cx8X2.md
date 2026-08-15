# Mutexes

Um mutex (bloco de exclusão mútua) é um primitivo de sincronização que garante que apenas uma thread possa acessar um recurso compartilhado, como uma variável ou estrutura de dados, por vez, prevenindo condições de corrida. Uma thread adquire (trava) o mutex antes de acessar o recurso compartilhado e libera (desbloqueia) ele após, e qualquer outra thread tentando travá-lo simultaneamente deve esperar. Esquecer de desbloquear um mutex ou travar o mesmo mutex duas vezes da mesma thread sem liberar-o primeiro pode causar um programa a ficar em deadlock, congelando indefinidamente.

Acesse os seguintes recursos para saber mais:

- [@article@Threads, Mutexes e Programação Concorrente em C](https://www.codequoi.com/en/threads-mutexes-and-concurrent-programming-in-c/)
- [@article@Usando mutexes](https://www.ibm.com/docs/en/aix/7.1.0?topic=programming-using-mutexes)
- [@video@Introdução ao Mutex (pthreads) | Tutorial de Programação em C](https://www.youtube.com/watch?v=raLCgPK-Igc)
