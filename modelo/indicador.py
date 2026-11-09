
class Indicador:
    def __init__ (self, codigo, fecha=None, valor=0.0, autor="", idUsuario=None, idIndicador=None):
        self.__idIndicador = idIndicador
        self.__idUsuario = idUsuario
        self.__autor = autor
        self.__codigo = codigo
        self.__fecha = fecha
        self.__valor = valor


    def __str__(self):
        return "{0} {1} {2}".format(self.__codigo, self.__fecha, self.__valor)


    #getters
    def getIdIndicador(self): return self.__idIndicador
    def getIdUsuario(self): return self.__idUsuario
    def getAutor(self): return self.__autor
    def getCodigo(self): return self.__codigo
    def getFecha(self): return self.__fecha
    def getValor(self): return self.__valor


    #setters
    def setIdIndicador(self, v): self.__idIndicador = v
    def setIdUsuario(self, v): self.__idUsuario = v
    def setAutor(self, v): self.__autor = v
    def setCodigo(self, v): self.__codigo = v
    def setFecha(self, v): self.__fecha = v
    def setValor(self, v): self.__valor = v