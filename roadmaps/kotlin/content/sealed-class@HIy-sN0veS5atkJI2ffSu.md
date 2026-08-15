# Classe Selada

Uma classe selada em Kotlin representa uma hierarquia de classes restrita. Ela é usada quando um valor pode ter um dos tipos limitados, mas nenhum outro tipo. Essencialmente, é uma classe abstrata que restringe quais classes podem herdar dela. Todas as subclasses de uma classe selada devem ser declaradas no mesmo arquivo em que a classe selada mesma. Esta restrição permite que o compilador saiba todos os possíveis subtipos em tempo de compilação, permitindo expressões `when` exaustivas.

Acesse os seguintes recursos para saber mais:

- [@oficial@Classes Seladas e Interfaces](https://kotlinlang.org/docs/sealed-classes.html)
- [@vídeo@Classes Seladas - Vocabulário Kotlin](https://www.youtube.com/watch?v=OyIRuxjBORY)
- [@vídeo@Classes Seladas VS. Classes Enum VS. Interfaces Seladas - Quando Usar Qual?](https://www.youtube.com/watch?v=kLJRZpRhX1o)
