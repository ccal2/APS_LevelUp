from flask import request
from utils.singleton import SingletonMeta
from adaptadores.adaptador_login_firebase import AdaptadorLoginFirebase


class Controlador(metaclass=SingletonMeta):
    def __init__(self):
        self.adaptador = AdaptadorLoginFirebase()

    def realizar_login(self):
        email = request.json.get("email", "")
        senha = request.json.get("senha", "")
        return self.adaptador.realizar_login(email, senha)
