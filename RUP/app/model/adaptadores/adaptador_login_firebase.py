from model.adaptadores.interface_login import InterfaceLogin
from SubsistemaComunicacaoAPILoginGoogle.i_subsistema_comunicacao_API_login_google import (
    ISubsistemaComunicacaoAPILoginGoogle,
)
from SubsistemaComunicacaoAPILoginGoogle.fachada_comunicacao_API_login_google import FachadaComunicacaoAPILoginGoogle


class AdaptadorLoginFirebase(InterfaceLogin):
    def __init__(self, servico: ISubsistemaComunicacaoAPILoginGoogle = None):
        if servico is None:
            self.servico = FachadaComunicacaoAPILoginGoogle()
        else:
            self.servico = servico

    def realizar_login(self, email: str, senha: str):
        resposta = self.servico.login(email=email, senha=senha)
        chaves_resposta = resposta.keys()

        mapaemento_erros = {
            "EMAIL_NOT_FOUND": "Email não cadastrado",
            "INVALID_PASSWORD": "Senha inválida",
            "USER_DISABLED": "Usuário não habilitado",
        }

        CHAVE_ERRO = "error"
        if CHAVE_ERRO in chaves_resposta:
            erro_servico = resposta[CHAVE_ERRO]["message"]
            return {"status": "erro", "mensagem": mapaemento_erros[erro_servico]}
        elif resposta.get("registered") == True:
            return {"status": "sucesso"}
        else:
            return {"status": "erro", "mensagem": "Algo deu errado"}
