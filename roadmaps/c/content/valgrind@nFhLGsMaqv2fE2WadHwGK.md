# Valgrind

Valgrind é uma ferramenta de análise dinâmica que executa um programa compilado dentro de um ambiente virtual para detectar erros de memória, como ler memória não inicializada, usar memória após ela ter sido liberada e vazamento de memória, em tempo de execução. Sua ferramenta mais comumente usada, Memcheck, relata a linha exata onde ocorreu um erro de memória, incluindo o ponto onde a memória envolvida foi originalmente alocada. Executar um programa sob Valgrind lenta significativamente sua execução, tornando-o mais adequado para testes do que uso em produção.

Acesse os seguintes recursos para saber mais:

- [@article@Guia sobre Valgrind](https://web.stanford.edu/class/archive/cs/cs107/cs107.1174/guide_valgrind.html)
- [@video@Depuração Dinâmica de Memória em C com Valgrind](https://www.youtube.com/watch?v=bb1bTJtgXrI)
