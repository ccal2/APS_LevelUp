from utils.singleton import SingletonMeta
from adaptadores.adaptador_login_firebase import AdaptadorLoginFirebase


class Controlador(metaclass=SingletonMeta):
    def __init__(self):
        self.adaptador = AdaptadorLoginFirebase

    def realizar_login(self, email: str, senha: str):
        self.adaptador.realizar_login(email, senha)
