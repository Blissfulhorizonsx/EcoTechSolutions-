import html
import re
from cryptography.fernet import Fernet # pip install cryptography


class ValidadorSeguridad:
    # La clave debe ser siempre la misma. Si cambia, no podrás descifrar
    # los salarios ya guardados. Genérala UNA vez y guárdala fuera del código.
    __clave = None

    def __init__(self):
        if ValidadorSeguridad.__clave is None:
            ValidadorSeguridad.__clave = self.__cargarClave()
        self.__fernet = Fernet(ValidadorSeguridad.__clave)

    @staticmethod
    def __cargarClave() -> bytes:
        try:
            with open("clave.key", "rb") as f:
                return f.read()
        except FileNotFoundError:
            clave = Fernet.generate_key()
            with open("clave.key", "wb") as f:
                f.write(clave)
            return clave

    def sanitizar_entrada(self, dato: str) -> str:
        """Limpia texto libre: quita espacios sobrantes, caracteres de control
        y escapa HTML. La defensa real contra inyección SQL son las consultas
        parametrizadas (%s) en los DAO; esto es una capa adicional."""
        if dato is None:
            return ""
        dato = str(dato).strip()
        dato = re.sub(r"[\x00-\x1f\x7f]", "", dato)
        return html.escape(dato)

    def cifrar_dato_sensible(self, dato: str) -> str:
        return self.__fernet.encrypt(str(dato).encode("utf-8")).decode("utf-8")

    def descifrar_dato_sensible(self, dato: str) -> str:
        return self.__fernet.decrypt(dato.encode("utf-8")).decode("utf-8")