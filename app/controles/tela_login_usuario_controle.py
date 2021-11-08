from model.fachadas.fachada import Fachada
from model.usuario.administrador.administrador import Administrador
from model.usuario.colaborador.colaborador import Colaborador


class TelaLoginUsuarioControle:
    def __init__(self):
        self.fachada = Fachada()
        self.tela = "TelaLoginUsuario.html"

    def realizar_login(self, email, senha):
        resultado_login = self.fachada.realizar_login(email=email, senha=senha)
        resposta = {}
        # se não for None, pode ser um erro, um Administrador ou um Colaborador
        if resultado_login is None:
            resposta["erro"] = "Usuário não encontrado"
        elif type(resultado_login) is Administrador:
            resposta["redirecionar"] = "/inicio/administrador"
        elif type(resultado_login) is Colaborador:
            resposta["redirecionar"] = "/inicio/colaborador"
        elif resultado_login.get("status") == "error":
            if resultado_login.get("message") == "INVALID_PASSWORD":
                resposta["erro"] = "Senha inválida"
            elif resultado_login.get("message") == "EMAIL_NOT_FOUND":
                resposta["erro"] = "Email não cadastrado"

        return resposta
