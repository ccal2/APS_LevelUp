import os
from dotenv import load_dotenv
import requests


class ControladorLogin:
    def login(self, email: str, senha: str):
        load_dotenv()
        CHAVE_API_LOGIN_GOOGLE = os.getenv("CHAVE_API_LOGIN_GOOGLE")
        LINK_DO_REQUEST = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={}"

        detalhes = {"email": email, "password": senha, "returnSecureToken": True}
        resultado = requests.post(LINK_DO_REQUEST.format(CHAVE_API_LOGIN_GOOGLE), data=detalhes)

        resultado_json = resultado.json()
        resultado_keys = resultado_json.keys()

        # check for errors
        CHAVE_ERRO = "error"
        if CHAVE_ERRO in resultado_keys:
            return {"status": "erro", "mensagem": resultado_json[CHAVE_ERRO]["message"]}

        # success
        CHAVE_IDTOKEN = "idToken"
        if CHAVE_IDTOKEN in resultado_keys:
            return {"status": "sucesso", CHAVE_IDTOKEN: resultado_json[CHAVE_IDTOKEN]}
