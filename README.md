# PS-2017-2-SI-Tarefas

## Descrição Informal dos Requisitos

O sistema de Controle de Tarefas tem como objetivo principal facilitar o controle das atividades gerenciadas por um grupo de pessoas que trabalham com manutenção de software.

Assim, para cada pessoa com acesso ao sistema, denominada usuário, existirá uma associação com um perfil, e cada perfil concede níveis de operação diferentes dentro do sistema. 

No sistema de Controle de Tarefas, foram definidos dois perfis de usuário, detalhados a seguir: 

	1. **Administrador:** Este perfil permite ao usuário a criação de tarefas e o acompanhamento (em tempo real) de todas as tarefas cadastradas no sistema;
	2. **Usuário:** O usuário com este perfil pode assumir tarefas e consequentemente mudar o status das tarefas para as quais ele é o responsável. 

Além das informações de usuário, o sistema também manterá os dados que permitem a identificação, autoria, responsabilidade e o controle dos possíveis estados de uma tarefa. 

Os estados das tarefas gerenciadas pelo sistema são: 

	1. **Cadastrada:** Este é o estado inicial de uma tarefa, atribuído na criação da tarefa por um usuário com perfil Administrador; 
	2. **Iniciada:** A tarefa neste estado foi iniciada por um usuário com perfil Usuário, que neste caso assumiu o papel de responsável por ela; 
	3. **Concluída:** Ao alcançar este estado, a tarefa foi concluída com sucesso pelo usuário responsável; 
	4. **Descartada:** Este estado conclui a tarefa com insucesso, indicando que o usuário responsável optou por anular a tarefa.

As tarefas são específicas de uma determina fase de um dado projeto, de forma que seja possível consultar as tarefas por projeto, por fase do projeto e por estado da tarefa.

Tarefas possuem um tipo, que pode ser: Defeito ou melhoria. Sendo que as tarefas classificadas como defeito devem ter prioridade de atendimento sobre as classificadas como melhoria.

Uma tarefa deve conter uma descrição do que deve ser feito, quem foi o relator da tarefa, a quem ela foi atribuída, qual o prazo deverá ser gasto para concluí-la e hora e com a respectiva data de conclusão calculada pelo sistema, considerando que um dia de trabalho corresponde a oito horas.

Quando o executor da tarefa alterar o seu estado para concluída, ele deverá informar o solução proposta para o problema descrito. Quanto tempo foi gasto e a data da conclusão do trabalho.

O sistema deverá permitir a consulta de tarefas em um determinado período. O usuário poderá filtrar estas tarefas por:

	1. Projeto
	2. Fase do projeto;
	3. Tipo da Tarefa;
	4. Estado;
	5. Relator
	6. Executor.
