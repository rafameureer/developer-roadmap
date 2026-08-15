# Vida Útil dos Objetos

A vida útil de um objeto é o período durante a execução do programa em que sua memória garante manter dados válidos. Variáveis locais na pilha geralmente vivem apenas até que o bloco circundante saia, variáveis estáticas e globais vivem por toda a duração do programa, e a memória alocada no heap vive até ser explicitamente liberada. Acessar um objeto fora de sua vida útil, como ler uma variável da pilha após a função ter retornado, produz comportamento indefinido.

Acesse os seguintes recursos para saber mais:

- [@artigo@Vida Útil](https://en.cppreference.com/c/language/lifetime#:~:text=Every%20object%20in%20C%20exists,known%20as%20this%20object's%20lifetime.)
