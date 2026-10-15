class Informe:
    def __init__(self, idUsuario, fchGeneracion=None, formato="", contenido="", idInforme=None):
        self.__idInforme = idInforme
        self.__fchGeneracion = fchGeneracion
        self.__formato = formato
        self.__contenido = contenido
        self.__idUsuario = idUsuario

    def __str__(self):
        return "{0} {1} {2}".format(self.__idInforme, self.__fchGeneracion, self.__formato)

    def getIdInforme(self): return self.__idInforme
    def getFchGeneracion(self): return self.__fchGeneracion
    def getFormato(self): return self.__formato
    def getContenido(self): return self.__contenido
    def getIdUsuario(self): return self.__idUsuario

    def setIdInforme(self, v): self.__idInforme = v
    def setFchGeneracion(self, v): self.__fchGeneracion = v
    def setFormato(self, v): self.__formato = v
    def setContenido(self, v): self.__contenido = v
    def setIdUsuario(self, v): self.__idUsuario = v