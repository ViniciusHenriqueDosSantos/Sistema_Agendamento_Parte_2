# Funcionalidade adicional

# O que foi escolhido:

A funcionalidade extra adicionada foi a de reserva recorrente. A ideia é que o usuário consiga, em uma única operação, reservar a mesma sala em vários dias dentro de um intervalo, escolhendo em quais dias da semana isso deve acontecer. Antes disso só era possível reservar um dia por vez, então para alguém que precisava reservar a sala todas as quartas, por exemplo, era muito difícil ter que reservar toda vez.

# Porque foi escolhido

A escolha da Fachada ocorreu porque foi possível aproveitar várias coisas que já tinham sido feitas no código (o proxy, as strategies e o repositório) para montar uma funcionalidade nova e limpa, sem precisar repetir lógica nem criar métodos novos no repositório. A fachada apenas costura o que já existia de um jeito diferente, e o `main.py` só precisa coletar as entradas do usuário e chamar um método.

# Como foi implementado

Para implementar isso foi utilizado o padrão Facade/Fachada. A classe nova é a `FacadeRecorrencia`, que está em `src/politicas.py`. Ela tem apenas um método, o `criar_recorencia`, que recebe sala, usuário, data inicial, data final, horário e a lista de dias da semana escolhida pelo usuário. Por dentro ela percorre o intervalo dia a dia, verifica se aquele dia da semana está na lista e então faz tudo que já era feito para a reserva única: escolhe a strategy correta (prioridade de professor ou primeira reserva), passa pelo proxy para validar, cria a reserva e salva no repositório. Se ocorrer conflito em algum dia, ela apenas imprime o erro daquela data e continua o loop, então o restante das datas ainda é reservado normalmente.

# Como usar

No menu o fluxo é: o usuário escolhe criar reserva normalmente, informa a sala, o usuário e o horário, e é perguntado se a reserva é única ou recorrente. Se escolher recorrente, devem ser informadas a data inicial e a data final no formato `AAAA-MM-DD`, e depois os dias da semana separados por vírgula, usando `0` para segunda, `1` para terça, e assim até `6` para domingo.
