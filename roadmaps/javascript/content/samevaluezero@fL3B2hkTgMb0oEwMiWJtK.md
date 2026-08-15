# SameValueZero
 
SameValueZero é um algoritmo de igualdade usado internamente pelo JavaScript em métodos como `Array.prototype.includes()` e comparação de chaves em `Map`. Ele se comporta como `===` mas trata `NaN` como igual a si mesmo. Diferentemente do `SameValue`, ele considera `+0` e `-0` como iguais.

Acesse os seguintes recursos para saber mais:

- [@article@Igualdade de mesmo valor zero](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Comparação_de_valores_e_igualdade#igualdade_de_mesmo_valor_zero)
