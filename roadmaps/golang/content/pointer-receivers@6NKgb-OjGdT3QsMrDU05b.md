# Ponteiros como Receitores

Os métodos recebem um ponteiro para uma estrutura em vez de uma cópia usando a sintaxe `func (p *Tipo) nomeDoMétodo()`. É necessário quando o método modifica o estado do receptor ou a estrutura é grande. O Go lida automaticamente com a conversão entre valor e ponteiro ao chamar métodos.

Acesse os seguintes recursos para saber mais:

- [@oficial@Ponteiros como Receitores](https://go.dev/tour/methods/4)
- [@artigo@Compreendendo Ponteiros e Valores em GoLang](https://medium.com/the-bug-shots/understanding-value-and-pointer-receivers-in-golang-82dd73a3eef9)
- [@artigo@Como definir métodos com ponteiros como receitores](https://labex.io/tutorials/go-how-to-define-methods-with-pointer-receivers-437937)
