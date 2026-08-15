# Alocação Dinâmica de Memória

A alocação dinâmica reserva memória na pilha em tempo de execução, quando a quantidade de memória necessária não é conhecida antecipadamente ou precisa durar além da função que a criou. O C fornece `malloc`, `calloc` e `realloc` para alocação e `free` para liberar a memória de volta ao sistema. Cada alocação bem-sucedida deve ser eventualmente acompanhada por exatamente uma chamada `free`. Usar memória após liberá-la ou liberá-la duas vezes ambos levam a comportamento indefinido.

Acesse os seguintes recursos para saber mais:

- [@artigo@Gerenciamento de Memória em C](https://www.w3schools.com/c/c_memory_management.php)
- [@artigo@Programação em C — Alocação Dinâmica de Memória](https://medium.com/@acamvproducingstudio/c-programming-dynamic-memory-allocation-86221e811379)
- [@vídeo@Alocação Dinâmica | Tutorial de Programação em C](https://www.youtube.com/watch?v=R0qIYWo8igs)
