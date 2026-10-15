class Asignacion:
    def __init__(self, idEmple, idProyecto, fechaAsignacion=None, idAsign=None):
        self.__idAsign = idAsign
        self.__fechaAsignacion = fechaAsignacion
        self.__idEmple = idEmple
        self.__idProyecto = idProyecto

    def __str__(self):
        return "{0} emp:{1} proy:{2} {3}".format(self.__idAsign, self.__idEmple,
                                                  self.__idProyecto, self.__fechaAsignacion)

    def getIdAsign(self): return self.__idAsign
    def getFechaAsignacion(self): return self.__fechaAsignacion
    def getIdEmple(self): return self.__idEmple
    def getIdProyecto(self): return self.__idProyecto

    def setIdAsign(self, v): self.__idAsign = v
    def setFechaAsignacion(self, v): self.__fechaAsignacion = v
    def setIdEmple(self, v): self.__idEmple = v
    def setIdProyecto(self, v): self.__idProyecto = v