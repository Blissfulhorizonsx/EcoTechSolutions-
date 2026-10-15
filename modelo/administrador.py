from modelo.usuario import Usuario


class Administrador(Usuario):
    def __init__(self, nombreUsuario, contrasena="", idUsuario=None):
        super().__init__(nombreUsuario, contrasena, "ADMIN", idUsuario)

    def esAdmin(self) -> bool:
        return self.getRol() == "ADMIN"