# Object.is
 
`Object.is()` é um método para comparar dois valores com um comportamento mais estrito do que `===`. Ele lida com duas casos de borda de maneira diferente: `Object.is(NaN, NaN)` retorna `true` (enquanto `NaN === NaN` é `false`), e `Object.is(+0, -0)` retorna `false` (enquanto `+0 === -0` é `true`). É útil quando a identidade de valor exato é necessária.

Acesse os seguintes recursos para saber mais:

- [@artigo@Object.is() - MDN](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Object/is)
