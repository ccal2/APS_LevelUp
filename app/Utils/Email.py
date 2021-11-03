import re

class Email:

    def __init__(self, email: str):
        self.email = email

    def validar(self) -> bool:
        return re.fullmatch(pattern=r"[^@]+@[^@]+\.[^@]+", string=self.email) is not None
