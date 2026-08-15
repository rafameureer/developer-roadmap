# remember / Estado

A função `remember` é uma função do Compose que mantém um valor entre recomposições dentro de um composável. Quando combinada com `mutableStateOf`, ela cria um holder de estado que dispara uma recomposição quando o valor muda. O estado local gerenciado com `remember` é adequado para estados da UI que não precisam sobreviver a alterações de configuração.

Acesse os seguintes recursos para saber mais:

- [@official@Estado e Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [@article@Entendendo remember em Jetpack Compose: Uma Profundidade Inicial](https://medium.com/@sandeepkella23/understanding-remember-in-jetpack-compose-a-deep-dive-from-first-principles-2587b2098323)
