# Sistema_Agendamento

Sistema de agendamento de salas para uma instituição, permitindo cadastrar salas e usuários, criar, alterar e cancelar reservas, além de gerar relatórios diários.


## Funcionalidades

- Cadastro de salas
- Cadastro de usuários
- Criação de reservas (única ou recorrente por dias da semana)
- Cancelamento de reservas
- Edição de reservas
- Consulta de disponibilidade
- Geração de relatório diário de reservas
- Listagem de salas e usuários
- Reserva de limpeza usando usuário de manutenção


## Requisitos Funcionais

- RF-01: Listar salas disponíveis em um intervalo de datas, informando os horários livres de cada sala.

- RF-02: Permitir que um usuário crie, modifique ou cancele uma reserva, informando sala, usuário, data (`AAAA-MM-DD`) e horário (`HH:MM`).

- RF-03: Detectar e impedir colisões de horário, não permitindo duas reservas confirmadas para a mesma sala, data e horário, exceto quando a política de prioridade permitir substituição.

- RF-04: Enviar notificação aos usuários envolvidos quando uma reserva for alterada ou cancelada.

- RF-05: Disponibilizar relatório diário contendo apenas reservas confirmadas e seus respectivos horários.

- Bônus: Permitir a criação de reserva de limpeza por meio de um decorator, usando um usuário fixo de manutenção.


## Regras de Negócio

- Reservas possuem duração fixa de 1 hora.
- Horários válidos para reservas: `08:00` às `17:00`.
- Não podem existir reservas confirmadas duplicadas para a mesma sala, data e horário.
- Professores possuem prioridade sobre usuários não professores.
- Professores podem substituir reservas feitas por usuários que não sejam professores.
- Tentativas inválidas devem exibir mensagens de erro claras.


## Tecnologias Utilizadas

- Python 3.10+
- Programação Orientada a Objetos (POO)


## Conceitos Utilizados

- Encapsulamento
- Herança
- Polimorfismo
- Classes Abstratas
- Factory
- Strategy
- Observer
- Singleton
- Proxy
- Decorator
- Facade


## Padrões de Projeto

- `Factory`: usado em `SalaFactory` e `UsuarioFactory` para criar diferentes tipos de salas e usuários.
- `Strategy`: usado em `PrimeiraReserva` e `PrioridadeProfessor` para selecionar a política de criação de reservas.
- `Observer`: usado em `ObserverUsuario` e `NotificadorReservas` para notificar alterações e cancelamentos de reservas.
- `Singleton`: usado em `RepositorioReservas` para manter um repositório único em memória, com controle de concorrência.
- `Proxy`: usado em `ProxyReserva` para centralizar validações antes da criação de reservas.
- `Decorator`: usado em `DecoratorLimpeza` para adicionar o comportamento de reserva de limpeza.
- `Facade`: usado em `FacadeRecorrencia` para simplificar a criação de reservas recorrentes em um intervalo de datas e dias da semana.



## Executando Localmente

Execute o programa:

```bash
python3 src/main.py
```

O menu interativo permite cadastrar salas e usuários, criar/modificar/cancelar reservas, consultar disponibilidade, gerar relatórios e criar reservas de limpeza.


## Estrutura do projeto

- `src/` - código-fonte
	- `main.py` - interface de linha de comando
	- `dados.py` - repositório e lógica de disponibilidade
	- `salas.py` - modelos de salas e factory
	- `usuarios.py` - modelos de usuários e factory
	- `reservas.py` - lógica da reserva e notificações
	- `politicas.py` - strategy, proxy, decorator e facade para criação de reservas
	- `relatorios.py` - geração de relatórios diários
	- `notificacoes.py` - mecanismo de observadores/notifications


## Exemplos de uso

- Cadastrar uma sala: menu → `1` → escolha tipo, andar, número

- Cadastrar usuário: menu → `2` → escolha tipo, nome

- Criar reserva: menu → `6` → informe `ID` da sala, `ID` do usuário e horário; escolha entre reserva única (informe a data) ou recorrente (informe data inicial, data final e os dias da semana, separados por vírgula, no intervalo `0` Segunda a `6` Domingo)

- Criar reserva de limpeza: menu → `10` → informe `ID` da sala, data e horário


## Exemplo de Menu

```text
1 - Cadastrar sala
2 - Cadastrar usuário
3 - Listar salas
4 - Listar usuários
5 - Listar salas disponíveis
6 - Criar reserva
7 - Modificar reserva
8 - Cancelar reserva
9 - Relatório diário
10 - Criar reserva de limpeza
0 - Sair
```


## Notas de Desenvolvimento

- As validações e regras de prioridade entre usuários estão implementadas em `politicas.py`.
- O sistema de notificações de mudanças utiliza o padrão Observer.
- A criação de usuários e salas utiliza Factory.
- As estratégias e regras de prioridade utilizam Strategy e Proxy.
- O repositório em memória utiliza Singleton com lock para controle básico de concorrência.
- A reserva de limpeza utiliza Decorator como extensão opcional do projeto.
- A reserva recorrente utiliza Facade (`FacadeRecorrencia`) para encapsular o loop de datas e a escolha de estratégia em uma única chamada.


## Autores

- Ana Beatriz Ribeiro Garcia
- Pedro Marx Amaral Abreu 