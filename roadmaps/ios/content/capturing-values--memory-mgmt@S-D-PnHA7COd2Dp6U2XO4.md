# Capturando Valores e Gestão de Memória

As closures capturam referências às variáveis e constantes do contexto em torno delas. Quando uma closure captura uma instância de classe, ela mantém uma referência forte por padrão, o que pode criar ciclos de retenção se a instância também manter a closure. Listas de captura usando `[weak self]` ou `[unowned self]` quebram esses ciclos e são um padrão necessário no desenvolvimento iOS em Swift.

Acesse os seguintes recursos para saber mais:

- [@artigo@Listas de Captura em Swift](https://www.hackingwithswift.com/articles/179/capture-lists-in-swift-whats-the-difference-between-weak-strong-and-unowned-references)
- [@artigo@Mecanismos de Captura de Closures em Swift](https://www.swiftbysundell.com/articles/swifts-closure-capturing-mechanics/)
