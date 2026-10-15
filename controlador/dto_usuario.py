import bcrypt # instalar con: pip install bcrypt
from modelo.usuario import Usuario
from dao.dao_usuario import DaoUsuario


class UsuarioDTO:

    def listarUsuarios(self) -> list:
        resultado = DaoUsuario().listarUsuarios()
        lista = []
        if resultado is not None:
            for u in resultado:
                lista.append(Usuario(u["nombreUsuario"], rol=u["rol"], idUsuario=u["idUsuario"]))
        return lista

    def buscarUsuario(self, nombreUsuario: str) -> Usuario:
        r = DaoUsuario().buscarUsuario(Usuario(nombreUsuario))
        return Usuario(r["nombreUsuario"], r["contrasenaHash"], r["rol"], r["idUsuario"]) if r is not None else None

    def validarLogin(self, nombreUsuario: str, clave: str) -> Usuario:
        r = DaoUsuario().buscarUsuario(Usuario(nombreUsuario))
        if r is not None and bcrypt.checkpw(clave.encode("utf-8"), r["contrasenaHash"].encode("utf-8")):
            return Usuario(r["nombreUsuario"], rol=r["rol"], idUsuario=r["idUsuario"])
        return None

    def agregarUsuario(self, nombreUsuario: str, clave: str, rol: str = "EMPLEADO") -> str:
        hash_ = bcrypt.hashpw(clave.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        return DaoUsuario().agregarUsuario(Usuario(nombreUsuario, hash_, rol))

    def actualizarUsuario(self, idUsuario: int, nombreUsuario: str, rol: str) -> str:
        return DaoUsuario().actualizarUsuario(Usuario(nombreUsuario, rol=rol, idUsuario=idUsuario))

    def cambiarPassword(self, idUsuario: int, nuevaClave: str) -> str:
        hash_ = bcrypt.hashpw(nuevaClave.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        return DaoUsuario().cambiarPassword(Usuario("", hash_, idUsuario=idUsuario))

    def eliminarUsuario(self, idUsuario: int) -> str:
        return DaoUsuario().eliminarUsuario(Usuario("", idUsuario=idUsuario))