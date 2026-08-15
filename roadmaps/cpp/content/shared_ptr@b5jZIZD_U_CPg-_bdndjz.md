# shared_ptr

`shared_ptr` é um ponteiro inteligente em C++ que gerencia memória alocada dinamicamente. Ele permite que múltiplos ponteiros possuam e compartilhem seguramente o mesmo objeto. Quando o último `shared_ptr` apontando para um objeto sai do escopo, o objeto gerenciado é automaticamente excluído, previnindo vazamentos de memória. Isso é feito mantendo um contador de referências que rastreia o número de instâncias de `shared_ptr` apontando para a mesma localização de memória.
