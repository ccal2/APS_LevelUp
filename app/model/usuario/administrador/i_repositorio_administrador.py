import abc
from typing import Optional

from model.usuario.administrador.administrador import Administrador


class IRepositorioAdministrador(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def consultar_administrador(self, email: str) -> Optional[Administrador]:
        return
