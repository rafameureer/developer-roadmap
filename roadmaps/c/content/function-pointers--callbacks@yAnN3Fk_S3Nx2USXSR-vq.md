# Ponteiros para funções & Callbacks

Um ponteiro para função armazena o endereço de uma função, permitindo que essa função seja chamada indiretamente, passada como um argumento ou armazenada em uma estrutura de dados, semelhante à forma como um ponteiro regular armazena o endereço de uma variável. Os callbacks usam isso para permitir que uma função invoque outra que é decidida em tempo de execução, um padrão usado por funções da biblioteca padrão como `qsort`, que aceita uma função de comparação como um callback. Esse mecanismo subjacente a mais padrões avançados em C, incluindo simular o dispatch orientado a objetos através de estruturas contendo ponteiros para funções.

Acesse os seguintes recursos para saber mais:

- [@article@Ponteiros para Funções](https://www.w3schools.com/c/c_functions_pointers.php)
- [@article@Tornando Ponteiros para Funções Usáveis em C](https://vandervoord.net/blog/2015/6/2/making-function-pointers-usable-in-c)
- [@video@Ponteiros para Funções em C](https://www.youtube.com/watch?v=BRsv3ZXoHto)
