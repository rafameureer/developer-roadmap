# Contêineres em C++

Os Contêineres em C++ são parte da Biblioteca Padrão de Modelos (STL) que fornecem estruturas de dados para armazenar e organizar dados. Existem vários tipos de contêineres, cada um com suas próprias características e casos de uso. Aqui, discutimos alguns dos contêineres mais comumente usados:

1\. Vector
----------

Os vetores são arrays dinâmicos que podem redimensionar-se conforme necessário. Eles armazenam elementos em uma localização de memória contígua, permitindo acesso rápido a elementos usando índices.

Exemplo
-------

    #include <iostream>
    #include <vector>
    
    int main() {
        std::vector<int> vec = {1, 2, 3, 4, 5};
    
        vec.push_back(6); // Adiciona um elemento no final
    
        std::cout << "O vetor contém:";
        for (int x : vec) {
            std::cout << ' ' << x;
        }
        std::cout << '\n';
    }
    

2\. List
--------

Uma lista é uma lista duplamente encadeada que permite inserir ou remover elementos em qualquer posição em tempo constante. Ela não suporta acesso aleatório. As listas são melhores do que vetores para cenários onde você precisa inserir ou remover elementos no meio com frequência.

Exemplo
-------

    #include <iostream>
    #include <list>
    
    int main() {
        std::list<int> lst = {1, 2, 3, 4, 5};
    
        lst.push_back(6); // Adiciona um elemento no final
        
        std::cout << "A lista contém:";
        for (int x : lst) {
            std::cout << ' ' << x;
        }
        std::cout << '\n';
    }
    

3\. Map
-------

Um map é um contêiner associativo que armazena pares chave-valor. Ele suporta a recuperação de valores com base em suas chaves. As chaves são ordenadas por padrão em ordem crescente.

Exemplo
-------

    #include <iostream>
    #include <map>
    
    int main() {
        std::map<std::string, int> m;
    
        m["one"] = 1;
        m["two"] = 2;
    
        std::cout << "O map contém:\n";
        for (const auto &pair : m) {
            std::cout << pair.first << ": " << pair.second << '\n';
        }
    }
    

4\. Unordered\_map
------------------

Semelhante a um map, um unordered map armazena pares chave-valor, mas é implementado usando uma tabela de dispersão. Isso significa que o unordered\_map tem desempenho médio mais rápido em comparação com o map, já que ele não mantém ordem ordenada. No entanto, o desempenho pior pode ser pior do que o map.

Exemplo
-------

    #include <iostream>
    #include <unordered_map>
    
    int main() {
        std::unordered_map<std::string, int> um;
    
        um["one"] = 1;
        um["two"] = 2;
    
        std::cout << "O unordered map contém:\n";
        for (const auto &pair : um) {
            std::cout << pair.first << ": " << pair.second << '\n';
        }
    }
    

Estes são apenas alguns exemplos de contêineres em C++. Existem outros tipos de contêineres, como `set`, `multiset`, `deque`, `stack`, `queue` e `priority_queue`. Cada contêiner tem seus próprios casos de uso e características únicas. Aprender sobre esses contêineres e quando usá-los pode aumentar significativamente sua eficiência e eficácia no uso do C++.
