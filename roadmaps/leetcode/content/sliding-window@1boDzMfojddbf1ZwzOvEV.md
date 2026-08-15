# Janela Deslizante

O padrão de janela deslizante é usado quando você precisa encontrar um subarray ou substring ótimo que satisfaça algum restrição. Em vez de verificar todas as possíveis subarrays do zero, você mantém uma janela com dois ponteiros e atualiza o resultado incrementalmente conforme a janela se expande ou encontra. Janelas de tamanho fixo são fáceis; janelas de tamanho variável requerem uma regra clara para quando diminuir da esquerda. Este estágio também apresenta a deque monótona, que estende o padrão de janela deslizante para problemas que precisam do máximo ou mínimo dentro da janela em cada passo.

Acesse os seguintes recursos para saber mais:

- [@artigo@Técnica de Janela Deslizante: Um Guia Completo](https://leetcode.com/discuss/post/3722472/sliding-window-technique-a-comprehensive-ix2k/)
- [@artigo@Janela Deslizante em 7 minutos | Padrão LeetCode](https://www.youtube.com/watch?v=y2d0VHdvfdc)
