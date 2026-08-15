# free

`free` é uma função padrão da biblioteca usada para desalocar um bloco de memória que foi anteriormente reservado na pilha. Quando você chama essa função, ela libera a memória especificada de volta ao sistema para que possa ser usada por outros propósitos no programa. Passar um ponteiro para o início de um bloco de memória previamente alocado para `free` marca efetivamente esse espaço como disponível, embora o próprio ponteiro permaneça inalterado e deve ser idealmente definido como `NULL` imediatamente após isso para prevenir o uso acidental de referências pendentes.

Acesse os seguintes recursos para saber mais:

- [@article@Desalocar Memória em C](https://www.w3schools.com/c/c_memory_deallocate.php)
- [@article@Função free() da biblioteca C](https://www.tutorialspoint.com/c_standard_library/c_function_free.htm)
- [@video@Liberando a Memória Alocada Dinamicamente usando free()](https://www.youtube.com/watch?v=qG0wUzuBI_A)
