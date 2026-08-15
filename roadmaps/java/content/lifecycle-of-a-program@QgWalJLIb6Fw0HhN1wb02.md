# Ciclo de Vida de um Programa

No Java, o ciclo de vida do programa consiste em várias fases distintas que trabalham juntas para executar código. O processo começa com os desenvolvedores escrevendo código-fonte Java em arquivos `.java` usando um IDE ou editor de texto. Esse código é então compilado pelo compilador Java (javac) em bytecode armazenado em arquivos `.class`, com verificação de sintaxe e tipos realizados durante a compilação. Quando o programa é executado, a Máquina Virtual Java (JVM) carrega esses arquivos de classe compilados para a memória através de um processo envolvendo a carga de dados binários, vinculação para verificação e preparação, e inicialização dos elementos da classe. A JVM então verifica a conformidade do bytecode com as políticas de segurança, realiza a compilação Just-In-Time (JIT) para traduzir o bytecode em código de máquina nativo para melhor desempenho, e executa as instruções do programa enquanto gerencia os recursos do sistema. Ao longo da execução, a JVM lida com coleta de lixo reutilizando memória dos objetos não utilizados, e finalmente libera todos os recursos ao término do programa. Esta arquitetura habilita a capacidade "escreva uma vez, execute em qualquer lugar" do Java, pois o bytecode pode ser executado em qualquer dispositivo com uma JVM compatível.

Acesse os seguintes recursos para saber mais:

- [@artigo@Ciclo de Vida de um Programa Java](https://www.startertutorials.com/corejava/life-cycle-java-program.html)
- [@artigo@Como a JVM Executa Código Java](https://www.cesarsotovalero.net/blog/how-the-jvm-executes-java-code.html)
- [@artigo@JIT vs. AOT Compilação em Java](https://bell-sw.com/blog/compilation-in-java-jit-vs-aot/)
