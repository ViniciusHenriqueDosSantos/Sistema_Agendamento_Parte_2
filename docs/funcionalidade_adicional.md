# Funcionalidade adicional

# O que escolhemos:
A funcionalidade extra que adicionamos foi a de reserva recorrente. A ideia é que o usuário consiga, em uma única operação, reservar a mesma sala em vários dias dentro de um intervalo, escolhendo em quais dias da semana isso deve acontecer. Antes disso só dava pra reservar um dia por vez, então pra alguém que precisava reservar a sala todas as quartas, por exemplo, era muito difícil ter que reserver toda vez.

# Porque escolhemos
A escolha da Fachada veio porque conseguimos aproveitar várias coisas que já tinham sido feitas no código (o proxy, as strategies, o repositório) pra montar uma funcionalidade nova e limpa, sem precisar repetir lógica nem criar métodos novos no repositório. A fachada só costura o que já existia de um jeito diferente, e o `main.py` só precisa coletar as entradas do usuário e chamar um método.


# Como implementamos
Pra implementar isso usamos o padrão Facade/Fachada. A classe nova é a `FacadeRecorrencia`, que está em `src/politicas.py`. Ela tem apenas um método, o `criar_recorencia`, que recebe sala, usuário, data inicial, data final, horário e a lista de dias da semana que o usuário escolheu. Por dentro ela percorre o intervalo dia a dia, vê se aquele dia da semana está na lista, e então faz tudo que já era feito pra reserva única: escolhe a strategy certa (prioridade de professor ou primeira reserva), passa pelo proxy pra validar, cria a reserva e salva no repositório. Se der conflito em algum dia ela só imprime o erro daquela data e continua o loop, então o resto das datas ainda é reservado normalmente.

# Como usar
No menu o fluxo é: o usuário escolhe criar reserva normalmente, informa a sala, o usuário e o horário, e é perguntado se a reserva é única ou recorrente. Se escolher recorrente, ele digita a data inicial e a data final no formato AAAA-MM-DD, e depois os dias da semana separados por vírgula, usando 0 pra segunda, 1 pra terça, e assim até 6 para  o domingo.