# TLS / SSL Encryption

A criptografia TLS/SSL no MongoDB fornece canais de comunicação seguros entre clientes e o servidor de banco de dados, bem como entre membros do conjunto de réplicas e componentes do cluster shard, garantindo que os dados transmitidos por redes sejam protegidos contra interceptação e adulteração. Esta segurança na camada de transporte criptografa todo o tráfego de rede usando protocolos criptográficos padrão da indústria, suporta autenticação baseada em certificados para maior segurança e pode ser configurada para autenticação mútua onde ambos o cliente e o servidor verificam as identidades um do outro. Implementar TLS/SSL é essencial para implantações de produção, especialmente em ambientes de nuvem ou quando as instâncias do MongoDB se comunicam em redes não confiáveis, pois isso previne ataques man-in-the-middle e garante a confidencialidade dos dados durante a transmissão.

Acesse os seguintes recursos para saber mais:

- [@course@Segurança da rede: Badge de Habilidade Gerenciada](https://learn.mongodb.com/courses/networking-security-self-managed)
- [@course@Segurança da rede: Badge de Habilidade do Atlas](https://learn.mongodb.com/courses/networking-security-atlas)
- [@official@TLS / SSL Encryption](https://www.mongodb.com/docs/manual/core/security-transport-encryption/)
- [@official@Configurar mongod e mongos para TLS/SSL](https://www.mongodb.com/docs/manual/tutorial/configure-ssl/)
- [@article@Como habilitar TLS/SSL no MongoDB](https://medium.com/mongoaudit/how-to-enable-tls-ssl-on-mongodb-d973a92cefa6)
