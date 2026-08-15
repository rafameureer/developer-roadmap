# const_cast

`const_cast` é um operador de casting em C++ que permite adicionar ou remover explicitamente o qualificador `const` ou `volatile` de um tipo de variável. Isso basicamente habilita você a modificar um objeto que foi inicialmente declarado como `const` ou passar um objeto `const` para uma função que espera um argumento não-`const`. É uma ferramenta poderosa, mas deve ser usada com cautela, pois modificar diretamente um objeto verdadeiramente `const` pode levar a comportamento indefinido.
