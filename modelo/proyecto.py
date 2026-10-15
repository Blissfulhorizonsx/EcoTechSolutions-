class Proyecto:
    def __init__(self, nombProyecto, descripProyecto="", fchInicio=None, idProyecto=None):
        self.__idProyecto = idProyecto
        self.__nombProyecto = nombProyecto
        self.__descripProyecto = descripProyecto
        self.__fchInicio = fchInicio

    def __str__(self):
        return "{0} {1} {2}".format(self.__idProyecto, self.__nombProyecto, self.__fchInicio)

    def getIdProyecto(self): return self.__idProyecto
    def getNombProyecto(self): return self.__nombProyecto
    def getDescripProyecto(self): return self.__descripProyecto
    def getFchInicio(self): return self.__fchInicio

    def setIdProyecto(self, v): self.__idProyecto = v
    def setNombProyecto(self, v): self.__nombProyecto = v
    def setDescripProyecto(self, v): self.__descripProyecto = v
    def setFchInicio(self, v): self.__fchInicio = v