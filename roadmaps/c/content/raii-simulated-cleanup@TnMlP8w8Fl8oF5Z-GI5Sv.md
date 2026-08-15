# Simulação de Limpeza com RAII

RAII (Resource Acquisition Is Initialization) é um padrão do C++ onde a limpeza de um recurso está vinculada automaticamente à vida útil de um objeto. O C não tem destrutores para fazer isso automaticamente, então garantias semelhantes de limpeza são simuladas manualmente, por exemplo, usando a instrução `goto` para pular para uma única seção de limpeza no final da função que libera todos os recursos alocados. Alguns compiladores também suportam uma extensão não padrão `__attribute__((cleanup))` que chama uma função especificada automaticamente quando uma variável sai do escopo. Ambos os métodos visam reduzir o risco de esquecer de liberar um recurso em um dos vários caminhos possíveis de saída de uma função.

Acesse os seguintes recursos para saber mais:

- [@artigo@RAII no C: Gerenciamento Automático de Recursos com Atributos do GCC](https://dev.to/ayush_saini/raii-in-c-automating-resource-management-with-gcc-attributes-3cgf)
