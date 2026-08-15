# Ponteiros com Maps & Slices

Maps e slices são tipos de referência - passá-los para funções não copia os dados subjacentes. Modificações dentro das funções afetam o original. Não há necessidade de ponteiros explícitos. No entanto, reatribuir a variável do slice/map por si só não afetará o chamador a menos que esteja usando um ponteiro.

Acesse os seguintes recursos para saber mais:

- [@official@Maps](https://go.dev/blog/maps)
- [@official@Ponteiros](https://go.dev/tour/moretypes/1)
- [@article@Slice Arrays Corretamente](https://labex.io/tutorials/go-how-to-slice-arrays-correctly-418936)
