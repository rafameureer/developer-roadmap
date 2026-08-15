# Configurações de Aplicativos e Configurações

No framework [ASP.NET](http://ASP.NET) Core, as configurações de aplicativos e configurações se referem ao processo de armazenamento e gerenciamento de configurações específicas do aplicativo e dados de configuração.

*   **Configurações de Aplicativos** refere-se aos pares chave-valor de dados que um aplicativo usa para configurar seu comportamento, como strings de conexão de banco de dados, chaves da API ou outras configurações. Essas configurações são geralmente armazenadas em arquivos de configuração, como `appsettings.json`, `appsettings.development.json` ou `appsettings.production.json`, e podem ser acessadas usando a interface IConfiguration.
    
*   **Configurações** refere-se ao processo de carregar e gerenciar as configurações de aplicativos, incluindo especificar a fonte das configurações e o formato dos arquivos de configuração. No [ASP.NET](http://ASP.NET) Core, a classe `Startup` é responsável por configurar as configurações do aplicativo e geralmente carrega dados de configuração de várias fontes, como arquivos JSON, variáveis de ambiente ou argumentos de linha de comando.

Acesse os seguintes recursos para saber mais:

- [@artigo@O que é Azure App Configuration?](https://learn.microsoft.com/en-us/azure/azure-app-configuration/overview)
- [@artigo@O que são Configurações de Aplicativos e como eu trabalho com elas?](https://support.procore.com/faq/what-are-app-configurations)
- [@artigo@Configuração & AppSettings](https://docs.servicestack.net/appsettings)
