# realloc

`realloc` é uma função usada para alterar o tamanho de um bloco de memória alocado anteriormente. Ela recebe um ponteiro para um bloco de memória existente e um novo tamanho como argumentos, então tenta redimensionar o bloco preservando seu conteúdo existente. Se a localização atual da memória não puder ser expandida, ela aloca um novo bloco do tamanho solicitado, copia os dados do antigo bloco para a nova localização, libera o antigo bloco e retorna um ponteiro para o novo bloco.

Acesse os seguintes recursos para saber mais:

- [@artigo@Realloc em C](https://www.w3schools.com/c/c_memory_reallocate.php)
- [@artigo@Biblioteca C - Função realloc()](https://www.tutorialspoint.com/c_standard_library/c_function_realloc.htm)
- [@vídeo@Explicação de Realloc em C explicada de forma fácil! 🚢](https://www.youtube.com/watch?v=rUXjvybSPWc)
