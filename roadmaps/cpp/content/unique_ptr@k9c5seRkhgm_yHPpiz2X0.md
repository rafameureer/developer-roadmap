# unique_ptr

O `unique_ptr` é um ponteiro inteligente em C++ que fornece propriedade exclusiva de um objeto alocado dinamicamente. Ele garante que apenas um `unique_ptr` possa apontar para um determinado objeto em qualquer momento, evitando vazamentos de memória ao deletar automaticamente o objeto gerenciado quando o `unique_ptr` sai do escopo ou é explicitamente resetado. A propriedade pode ser transferida para outro `unique_ptr` usando `std::move`, mas a cópia é proibida para garantir o princípio da propriedade única.

Acesse os seguintes recursos para saber mais:

- [@official@std::unique_ptr - Referência Detalhada](https://en.cppreference.com/w/cpp/memory/unique_ptr)
- [@article@Ponteiros Inteligentes – unique_ptr](https://www.learncpp.com/cpp-tutorial/stdunique_ptr/)
- [@video@Quando você deve usar std::unique_ptr? - Discussão no StackOverflow](https://stackoverflow.com/questions/13782051/when-should-you-use-stdunique-ptr)
