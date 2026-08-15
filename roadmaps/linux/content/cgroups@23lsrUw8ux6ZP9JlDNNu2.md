# Grupos de Controle (Cgroups)

Grupos de Controle (cgroups) são uma funcionalidade do kernel Linux que organiza processos em grupos hierárquicos e limita seu uso de recursos (CPU, memória, E/S de disco). Essencial para a containerização, cgroups impedem que os contêineres monopolizem os recursos do host, garantindo a estabilidade e desempenho do sistema. Use `cgcreate` para criar grupos, atribuir processos e definir limites de recursos de forma eficaz.

Acesse os seguintes recursos para saber mais:

- [@official@Grupos de Controle — O Kernel Linux](https://docs.kernel.org/admin-guide/cgroup-v1/)
- [@article@cgroups — Página manual do Linux](https://www.man7.org/linux/man-pages/man7/cgroups.7.html)
- [@article@Introdução aos Grupos de Controle (Cgroups)](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/resource_management_guide/chap-introduction_to_control_groups)
