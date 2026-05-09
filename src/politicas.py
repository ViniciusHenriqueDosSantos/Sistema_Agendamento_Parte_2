from abc import ABC, abstractmethod
from datetime import date, time

from salas import Sala
from usuarios import Usuario, Professor
from reservas import Reserva


class StrategyReserva(ABC):
    """Interface para estratégias de criação de reserva."""

    @abstractmethod
    def nova_reserva(self, sala: Sala, usuario: Usuario, data: date, horario: time) -> Reserva | None:
        pass

class PrimeiraReserva(StrategyReserva):
    """Cria uma nova reserva quando ainda não existe reserva no horário."""

    def nova_reserva(self, sala: Sala, usuario: Usuario, data: date, horario: time) -> Reserva:
        return Reserva(sala, usuario, data, horario)


class PrioridadeProfessor(StrategyReserva):
    """Permite que professor tenha prioridade sobre uma reserva existente."""

    def nova_reserva(self, sala: Sala, usuario: Usuario, data: date, horario: time) -> Reserva | None:
        reserva = GetReserva.get_reserva(sala, data, horario)
        reserva.set_usuario(usuario)
        return reserva

class ProxyReserva:
    """Controla o acesso à criação de reservas."""

    def criar_reserva(self, sala: Sala, usuario:Usuario, data: date, horario: time) -> Reserva | None:
        reserva = GetReserva.get_reserva(sala, data, horario)

        if reserva is None:
            strategy = PrimeiraReserva()
            return strategy.nova_reserva(sala, usuario, data, horario)

        if isinstance(usuario, Professor):
            strategy = PrioridadeProfessor()
            return strategy.nova_reserva(sala, usuario, data, horario)

        return None


class GetReserva:
    """Classe responsável por buscar reservas existentes."""

    @staticmethod
    def get_reserva(sala: Sala,data: date,horario: time) -> Reserva | None:
        return None