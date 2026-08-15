# Máquinas de Aumento Gradual

As Máquinas de Aumento Gradual (Gradient Boosting Machines) são um método de aprendizado em conjunto que combina várias aprendizes fracos, típicamente árvores de decisão, para criar um modelo preditivo forte para tarefas de classificação. O algoritmo funciona iterativamente, com cada nova árvore treinada para corrigir os erros cometidos pelas árvores anteriores. Isso é feito focando-se nas instâncias que foram mal classificadas nas iterações anteriores, efetivamente "aumentando" o desempenho do modelo. Implementações populares de aumento gradual incluem XGBoost, LightGBM, CatBoost e o original GradientBoostingClassifier, cada um oferecendo variações em regularização, estratégias de crescimento de árvores e tratamento de características categóricas.

Acesse os seguintes recursos para saber mais:

- [@artigo@Classificador de Aumento Gradual | scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)
- [@artigo@Um guia para o Algoritmo de Aumento Gradual](https://www.datacamp.com/tutorial/guide-to-the-gradient-boosting-algorithm)
- [@artigo@Algoritmos de Aumento em Aprendizado de Máquina, Parte I: AdaBoost](https://medium.com/data-science/boosting-algorithms-in-machine-learning-part-i-adaboost-b9d86041a521)
- [@artigo@Algoritmos de Aumento em Aprendizado de Máquina, Parte II: Aumento Gradual](https://towardsdatascience.com/boosting-algorithms-in-machine-learning-part-ii-gradient-boosting-c155ae505fe9/)
- [@artigo@Aumento Gradual no scikit-learn: Tutorial Prático](https://www.youtube.com/watch?v=E2mCaIZNE2g)
