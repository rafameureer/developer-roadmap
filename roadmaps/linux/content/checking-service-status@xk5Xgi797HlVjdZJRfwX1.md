# Verificando o Status do Serviço

`systemctl status nome-do-servico` fornece um instantâneo em tempo real de um serviço: se ele está ativo, inativo ou falhou; seu ID de processo; as últimas linhas de log; e quaisquer mensagens de erro da última execução. Para uma verificação rápida booleana, `systemctl is-active` e `systemctl is-enabled` retornam valores simples adequados para uso em scripts. O estado habilitado/desabilitado indica se o serviço está configurado para iniciar automaticamente no boot, separadamente do fato de estar atualmente em execução.

Acesse os seguintes recursos para saber mais:

- [@article@Verificando o Status de um Serviço Sem Ter Um Nome Exato](https://www.baeldung.com/linux/initialization-managers-service-status)
