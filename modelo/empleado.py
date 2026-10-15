from modelo.usuario import Usuario
from seguridad.validador_seguridad import ValidadorSeguridad

class Empleado(Usuario):
    def __init__(self, nombEmplea, direccEmple="", numEmple="", mailEmple="",
                 fchContrato=None, salarioCifrado="", idDepart=None,
                 idUsuario=None, idEmple=None, nombreUsuario="", contrasena=""):
        
        super().__init__(nombreUsuario, contrasena, "EMPLEADO", idUsuario)
        
        self.__idEmple = idEmple
        self.__nombEmplea = nombEmplea
        self.__direccEmple = direccEmple
        self.__numEmple = numEmple
        self.__mailEmple = mailEmple
        self.__fchContrato = fchContrato
        self.__salarioCifrado = salarioCifrado
        self.__idDepart = idDepart

    def __str__(self):
        return "{0} {1} {2}".format(self.__idEmple, self.__nombEmplea, self.__mailEmple)

    def obtenerSalarioDescifrado(self) -> float:
        if not self.__salarioCifrado:
            return 0.0
        return float(ValidadorSeguridad().descifrar_dato_sensible(self.__salarioCifrado))

    # Getters
    def getIdEmple(self): return self.__idEmple
    def getNombEmplea(self): return self.__nombEmplea
    def getDireccEmple(self): return self.__direccEmple
    def getNumEmple(self): return self.__numEmple
    def getMailEmple(self): return self.__mailEmple
    def getFchContrato(self): return self.__fchContrato
    def getSalarioCifrado(self): return self.__salarioCifrado
    def getIdDepart(self): return self.__idDepart

    # Setters
    def setIdEmple(self, v): self.__idEmple = v
    def setNombEmplea(self, v): self.__nombEmplea = v
    def setDireccEmple(self, v): self.__direccEmple = v
    def setNumEmple(self, v): self.__numEmple = v
    def setMailEmple(self, v): self.__mailEmple = v
    def setFchContrato(self, v): self.__fchContrato = v
    def setSalarioCifrado(self, v): self.__salarioCifrado = v
    def setIdDepart(self, v): self.__idDepart = v