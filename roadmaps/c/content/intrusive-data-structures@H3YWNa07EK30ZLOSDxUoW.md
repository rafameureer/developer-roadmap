# Estruturas de Dados Intrusivas

Uma estrutura de dados intrusiva incorpora os elementos estruturais necessários para um contêiner, como o ponteiro next para uma lista encadeada, diretamente dentro do tipo de dado sendo armazenado, em vez de envolver os dados em um nó de contêiner separado. Isso evita a alocação extra de memória para nós específicos de contêiner e permite que o mesmo pedaço de dados pertença a várias estruturas intrusivas simultaneamente. O núcleo do Linux usa intensivamente esse padrão para suas listas encadeadas internas.
