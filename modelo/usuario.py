class Usuario:
    def __init__(self, nombreUsuario, contrasena="", rol="EMPLEADO", idUsuario=None):
        self.__idUsuario = idUsuario
        self.__nombreUsuario = nombreUsuario
        self.__contrasena = contrasena   
        self.__rol = rol

    def __str__(self):
        return "{0} {1} {2}".format(self.__idUsuario, self.__nombreUsuario, self.__rol)

    def getIdUsuario(self):
        return self.__idUsuario
    def getNombreUsuario(self):
        return self.__nombreUsuario
    def getContrasena(self):
        return self.__contrasena
    def getContrasenaHash(self):
        return self.__contrasena
    def getRol(self):
        return self.__rol

    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario
    def setNombreUsuario(self, nombreUsuario):
        self.__nombreUsuario = nombreUsuario
    def setContrasena(self, contrasena):
        self.__contrasena = contrasena
    def getContresenaHash(self, contrasena):
        self.__contrasena = contrasena
    def setRol(self, rol):
        self.__rol = rol