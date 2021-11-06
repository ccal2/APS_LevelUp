import os
from dotenv import load_dotenv
import requests


class ControladorLogin:
    def login(self, email: str, senha: str):
        load_dotenv()
        CHAVE_API_LOGIN_GOOGLE = os.getenv("CHAVE_API_LOGIN_GOOGLE")
        LINK_DO_REQUEST = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={}"

        detalhes = {"email": email, "password": senha, "returnSecureToken": True}
        request = requests.post(LINK_DO_REQUEST.format(CHAVE_API_LOGIN_GOOGLE), data=detalhes)

        request_json = request.json()
        request_keys = request_json.keys()

        # check for errors
        CHAVE_ERRO = "error"
        if CHAVE_ERRO in request_keys:
            return {"status": "error", "message": request_json[CHAVE_ERRO]["message"]}

        # success
        CHAVE_IDTOKEN = "idToken"
        if CHAVE_IDTOKEN in request_keys:
            return {"status": "success", CHAVE_IDTOKEN: request_json[CHAVE_IDTOKEN]}
