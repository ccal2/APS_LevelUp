from adaptadores.interface_login import InterfaceLogin
from comunicacao.api_login_firebase import APILoginFirebase


class AdaptadorLoginFirebase(InterfaceLogin):
    def __init__(self):
        self.servico = APILoginFirebase()

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
            return {"erro": mapaemento_erros[erro_servico]}
        elif resposta.get("registered") == True:
            return {}
        else:
            return {"erro": "Algo deu errado"}
