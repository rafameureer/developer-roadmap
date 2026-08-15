# Pacotes

Um pacote é um namespace que principalmente contém classes e interfaces. Por exemplo, a classe padrão `ArrayList` está no pacote `java.util`. Para essa classe, `java.util.ArrayList` é chamado de nome qualificado completo porque esta sintaxe não tem ambiguidade. Classes em diferentes pacotes podem ter o mesmo nome. Por exemplo, você tem as duas classes `java.util.Date` e `java.sql.Date`, que são diferentes. Se nenhuma declaração de pacote for feita em uma classe, seu pacote será o pacote padrão.

Para criar um pacote use este comando -> javac -d diretório nome_do_arquivo.java

Acesse os seguintes recursos para saber mais:

- [@artigo@Pacotes em Java](https://docs.oracle.com/javase/8/docs/api/java/lang/Package.html)
