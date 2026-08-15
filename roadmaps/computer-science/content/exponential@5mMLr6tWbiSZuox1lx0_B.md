# Exponencial

Algoritmos exponenciais são aqueles que crescem em uma taxa de 2^n. Isso significa que para cada entrada adicional, o algoritmo levará o dobro do tempo para ser executado. A seguinte função é um exemplo de um algoritmo exponencial:

    def exponential(n):
        if n == 0:
            return 1
        return exponential(n - 1) + exponential(n - 1)
    

Como você pode ver, o tempo de execução do algoritmo cresce exponencialmente. Para cada entrada adicional, o algoritmo levará o dobro do tempo para ser executado.

Acesse os seguintes recursos para saber mais:

- [@vídeo@Notação Big O — Calculando Complexidade Temporal](https://www.youtube.com/watch?v=Z0bH0cMY0E8)
- [@vídeo@Notações Big O](https://www.youtube.com/watch?v=V6mKVRU1evU)
