# Ponteiros void

Um ponteiro `void`, declarado como `void *`, pode apontar para qualquer tipo de dados, mas não pode ser desreferenciado diretamente, pois o compilador não tem informações sobre o tipo de dados ao que ele está apontando. Geralmente é convertido em um tipo de ponteiro específico antes de uso e aparece frequentemente em funções genéricas como `malloc`, que retorna `void *` porque não sabe qual tipo de dado será armazenado lá. Essa flexibilidade vem com o custo de perder a segurança do tipo até que a conversão aconteça.

Acesse os seguintes recursos para saber mais:

- [@article@Ponteiro void em C](https://www.tutorialspoint.com/cprogramming/c_void_pointer.htm)
- [@video@Entendendo ponteiros void](https://www.youtube.com/watch?v=ij2jrsUmwCI)
