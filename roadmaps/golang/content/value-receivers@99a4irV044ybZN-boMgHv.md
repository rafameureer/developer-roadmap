# Receivers de Valor

Os métodos recebem uma cópia da estrutura em vez de um ponteiro. Use a sintaxe `func (v Tipo) methodName()`. Apropriado quando o método não modifica o receptor ou a estrutura é pequena. Pode ser chamado tanto por valores quanto por ponteiros, com Go automaticamente desreferenciando.

Acesse os seguintes recursos para saber mais:

- [@official@Receivers de Valor](https://go.dev/tour/methods/8)
- [@article@Compreendendo Receivers de Valor e Ponteiro em Interfaces do Go](https://afdz.medium.com/understanding-value-and-pointer-receivers-in-go-interfaces-e97a824fdded)
- [@article@Receptores de Método em Go: Compreendendo Valor vs. Ponteiro e Quando Usar Cada Um](https://blog.stackademic.com/go-method-receivers-understanding-value-vs-pointer-and-when-to-use-each-74ef82d66a5c)
