# Fase Ampla

**Fase de Colisão Ampla (Broad Phase Collision Detection)** é o primeiro passo no processo de detecção de colisões. Sua função principal é identificar quais pares de objetos podem potencialmente colidir. Em vez de examinar todo o corpo de cada objeto em busca de possíveis colisões, ele envolve cada um em uma forma mais simples como uma caixa limitante ou esfera, com o objetivo de reduzir o número de cálculos. A saída desta fase é uma lista de 'pares candidatos' que são passados para a próxima fase, geralmente referida como a fase estreita (narrow phase), para verificações mais profundas de sobreposição.

Acesse os seguintes recursos para saber mais:

- [@artigo@Fase Ampla de Detecção de Colisão](http://buildnewgames.com/broad-phase-collision-detection/)
