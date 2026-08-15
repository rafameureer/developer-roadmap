# Dados de Treinamento e Teste

Quando criamos um modelo de aprendizado de máquina, geralmente dividimos nosso conjunto de dados em duas partes: um conjunto de treinamento e um conjunto de teste. O conjunto de treinamento é usado para ensinar o modelo como fazer previsões, enquanto o conjunto de teste é usado para avaliar como bem o modelo aprendeu. Isso nos ajuda a entender se o modelo pode generalizar para novos dados não vistos. No scikit-learn, você pode facilmente dividir seus dados usando a função `train_test_split` do módulo `model_selection`. Você fornece seus dados e rótulos para essa função, e ela retorna os conjuntos de dados divididos. Você também pode especificar a proporção dos dados a serem usados para teste.

Acesse os seguintes recursos para saber mais:

- [@oficial@train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
- [@artigo@Dividindo seu conjunto de dados com train_test_split() do scikit-learn](https://realpython.com/train-test-split-python-data/)
- [@vídeo@Divisão de Treinamento e Teste com Python Machine Learning (Scikit-Learn)](https://www.youtube.com/watch?v=SjOfbbfI2qY)
