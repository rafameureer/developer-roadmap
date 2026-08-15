# Chamada de Função Gemini

A chamada de função Gemini permite que você conecte o modelo linguístico Gemini a código real de uma maneira segura e simples. Primeiro, você lista as funções que deseja que ele use, cada uma com um nome, uma breve nota sobre o que ela faz e um esquema JSON para os argumentos necessários. Quando o usuário fala, Gemini verifica esta lista e, se uma correspondência faz sentido, responde com um pequeno bloco de JSON que contém o nome da função escolhida e os argumentos preenchidos. Seu programa então executa aquela função, envia o resultado de volta e a conversa continua. Porque a resposta é estrito JSON e não texto livre, você não precisa adivinhar o que o modelo significa e evita muitos erros. Este fluxo permite que você crie agentes que busquem dados, chamem APIs ou execute longas cadeias de ações enquanto mantém o controle da lógica de negócios em seu lado.

Acesse os seguintes recursos para saber mais:

- [@official@Chamada de Função com a API Gemini](https://ai.google.dev/gemini-api/docs/function-calling)
- [@article@Entendendo Chamada de Função no Gemini](https://medium.com/google-cloud/understanding-function-calling-in-gemini-3097937f1905)
