from model.controladores.controlador_login_usuario import ControladorLoginUsuario

class Fachada:
    def __init__(self):
        self.controlador_login_usuario = ControladorLoginUsuario()

    def realizar_login(self, email: str, senha: str):  #  -> Optional[Usuario] | str
        return self.controlador_login_usuario.realizar_login(email, senha)
