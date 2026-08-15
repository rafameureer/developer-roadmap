# weak_ptr

`weak_ptr` é um ponteiro inteligente em C++ que mantém uma referência não proprietária a um objeto gerenciado por um `shared_ptr`. Ele não participa do contagem de propriedade do objeto, o que significa que ele não impede o objeto de ser destruído se os `shared_ptr`s que possuem o objeto saírem do escopo. Seu uso principal é para detectar se o objeto gerenciado pelo `shared_ptr` ainda existe. Você pode obter um `shared_ptr` a partir de um `weak_ptr` usando `lock()`, mas isso pode retornar um `shared_ptr` vazio se o objeto já tiver sido destruído.
