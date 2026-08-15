# Conversão de Slice para Array

Converta um slice em um array usando `[N]T(slice)` (Go 1.17+). Copia os dados do slice para um array de tamanho fixo. Panic se o slice tiver menos de N elementos. Útil quando são necessas as semânticas de array ou garantias específicas de tamanho.

Acesse os seguintes recursos para saber mais:

- [@artigo@Manipulando Arrays Corretamente](https://labex.io/tutorials/go-how-to-slice-arrays-correctly-418936)
- [@artigo@Go - Criar Slice a partir de Array - 3 Exemplos](https://www.tutorialkart.com/golang-tutorial/golang-create-slice-from-array/)
