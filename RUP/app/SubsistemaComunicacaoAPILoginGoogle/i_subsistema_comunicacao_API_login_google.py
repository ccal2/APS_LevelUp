import abc


class ISubsistemaComunicacaoAPILoginGoogle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def login(self, email: str, senha: str):
        return
