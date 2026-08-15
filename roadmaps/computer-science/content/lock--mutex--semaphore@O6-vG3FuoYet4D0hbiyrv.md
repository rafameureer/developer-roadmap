# Lock / Mutex / Semaphore

Um lock permite que apenas uma thread entre na parte que está bloqueada e o lock não é compartilhado com nenhum outro processo.

Um mutex é o mesmo que um lock, mas pode ser de escopo global (compartilhado por vários processos).

Um semaphore faz a mesma coisa que um mutex, mas permite x número de threads entrar. Isso pode ser usado, por exemplo, para limitar o número de tarefas intensivas em CPU, I/O ou RAM sendo executadas simultaneamente.

Acesse os seguintes recursos para saber mais:

- [@article@O que é a diferença entre lock, mutex e semaphore?](https://stackoverflow.com/questions/2332765/what-is-the-difference-between-lock-mutex-and-semaphore)
- [@article@O que é um Semaphore](https://stackoverflow.com/questions/34519/what-is-a-semaphore/40238#40238)
