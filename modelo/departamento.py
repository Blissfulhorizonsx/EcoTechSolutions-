class Departamento:
    def __init__(self, nombDepart, gerentDepart="", idDepart=None):
        self.__idDepart = idDepart
        self.__nombDepart = nombDepart
        self.__gerentDepart = gerentDepart

    def __str__(self):
        return "{0} {1} {2}".format(self.__idDepart, self.__nombDepart, self.__gerentDepart)

    def getIdDepart(self): return self.__idDepart
    def getNombDepart(self): return self.__nombDepart
    def getGerentDepart(self): return self.__gerentDepart

    def setIdDepart(self, v): self.__idDepart = v
    def setNombDepart(self, v): self.__nombDepart = v
    def setGerentDepart(self, v): self.__gerentDepart = v