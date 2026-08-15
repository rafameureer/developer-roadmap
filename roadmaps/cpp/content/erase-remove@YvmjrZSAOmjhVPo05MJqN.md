# Erase-Remove

O idiom Erase-Remove é uma técnica comum em C++ usada para remover eficientemente elementos de um contêiner (como `std::vector`, `std::list`, etc.). Involves usar `std::remove` (ou `std::remove_if`) para mover os elementos a serem removidos para o final do contêiner, seguido pelo uso do método `erase()` do contêiner para remover efetivamente esses elementos, reduzindo assim o tamanho do contêiner.

Acesse os seguintes recursos para saber mais:

- [@article@std::remove, std::remove_if](https://en.cppreference.com/w/cpp/algorithm/remove.html)
- [@video@C++ STL algorithm - erase-remove idiom -- std::remove(_if, _copy_if) | Modern Cpp Series Ep. 154](https://www.youtube.com/watch?v=btyuTSb_238)
