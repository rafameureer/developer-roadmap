# Instalação do Plano de Controle

Os componentes do plano de controle tomam decisões globais sobre o cluster (por exemplo, escalonamento), além de detectar e responder a eventos de cluster (por exemplo, iniciando um novo pod quando o campo réplicas de uma implantação não está satisfeito). Os componentes do plano de controle podem ser executados em qualquer máquina no cluster. No entanto, para simplicidade, scripts de configuração típicos iniciam todos os componentes do plano de controle na mesma máquina e não executam contêineres de usuário nesta máquina.

Acesse os seguintes recursos para saber mais:

- [@oficial@Inicializando seu nó de plano de controle - Documentação](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#initializing-your-control-plane-node)
- [@vídeo@Tutorial - Instalar Componentes do Plano de Controle](https://www.youtube.com/watch?v=IUwuyZ5ReF0)
