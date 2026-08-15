# Fatorial

Algoritmos com complexidade fatorial têm um tempo de execução de `O(n!)`. Este é o pior cenário para um algoritmo. Algoritmos com complexidade fatorial são muito ineficientes e devem ser evitados.

    def generate_permutations(s):
        # Caso base: Se a comprimento da string for 1, retorne uma lista contendo a string
        if len(s) == 1:
            return [s]
    
        # Inicialize a lista de resultados
        permutations = []
    
        # Gere recursivamente todas as permutações
        for i in range(len(s)):
            # Caractere atual
            current_char = s[i]
            # Caracteres restantes
            remaining_chars = s[:i] + s[i + 1 :]
            # Gere todas as permutações dos caracteres restantes
            for perm in generate_permutations(remaining_chars):
                # Adicione o caractere atual à frente de cada permutação gerada
                permutations.append(current_char + perm)
    
        return permutations

Acesse os seguintes recursos para saber mais:

- [@artigo@Folha de Dicas Big O - Gráfico de Complexidade Temporal](https://www.freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart/)
- [@vídeo@Fatorial Explicado](https://www.youtube.com/watch?v=pxh__ugRKz8)
