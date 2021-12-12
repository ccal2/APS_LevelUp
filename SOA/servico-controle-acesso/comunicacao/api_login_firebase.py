import os
from dotenv import load_dotenv
import requests


class APILoginFirebase:
    def __init__(self):
        load_dotenv()
        self.chave_api = os.getenv("CHAVE_API_LOGIN_GOOGLE")
        self.url_base = "https://identitytoolkit.googleapis.com/v1"

    def login(self, email: str, senha: str):
        LINK_DO_REQUEST = f"{self.url_base}/accounts:signInWithPassword?key={}"

        detalhes = {"email": email, "password": senha, "returnSecureToken": True}
        resultado = requests.post(LINK_DO_REQUEST.format(self.chave_api), data=detalhes)

        return resultado.json()
