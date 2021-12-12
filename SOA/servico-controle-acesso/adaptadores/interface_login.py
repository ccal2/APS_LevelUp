import abc


class InterfaceLogin(metaclass=abc.ABCMeta):

    """
    Retorno:
    - sucesso:
        {}
    - erro:
        {
            "erro": <mensagem de erro>
        }
        mensagens de erro:
            - "Email não cadastrado"
            - "Senha inválida",
            - "Usuário não habilitado"
    """

    @abc.abstractmethod
    def realizar_login(self, email: str, senha: str):
        return
