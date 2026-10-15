from datetime import timedelta, datetime


class RegistroTiempo:
    def __init__(self, idEmple, idProyecto, fchTrabajo=None, horaInicio=None,
                 horaTermino=None, descripTareas="", idRegistro=None):
        self.__idRegistro = idRegistro
        self.__fchTrabajo = fchTrabajo
        self.__horaInicio = horaInicio
        self.__horaTermino = horaTermino
        self.__descripTareas = descripTareas
        self.__idEmple = idEmple
        self.__idProyecto = idProyecto

    def __str__(self):
        return "{0} {1} {2}".format(self.__idRegistro, self.__fchTrabajo, self.calcularHoras())

    @staticmethod
    def __aTimedelta(valor):
        # MySQL entrega TIME como timedelta; desde la vista puede venir como "HH:MM"
        if isinstance(valor, timedelta):
            return valor
        t = datetime.strptime(str(valor)[:5], "%H:%M")
        return timedelta(hours=t.hour, minutes=t.minute)

    def calcularHoras(self) -> str:
        """Devuelve las horas trabajadas en formato HH:MM (ej: 08:30)."""
        if self.__horaInicio is None or self.__horaTermino is None:
            return "00:00"
        dif = self.__aTimedelta(self.__horaTermino) - self.__aTimedelta(self.__horaInicio)
        total = int(dif.total_seconds() // 60)
        return "{0:02d}:{1:02d}".format(total // 60, total % 60)

    def getIdRegistro(self): return self.__idRegistro
    def getFchTrabajo(self): return self.__fchTrabajo
    def getHoraInicio(self): return self.__horaInicio
    def getHoraTermino(self): return self.__horaTermino
    def getDescripTareas(self): return self.__descripTareas
    def getIdEmple(self): return self.__idEmple
    def getIdProyecto(self): return self.__idProyecto

    def setIdRegistro(self, v): self.__idRegistro = v
    def setFchTrabajo(self, v): self.__fchTrabajo = v
    def setHoraInicio(self, v): self.__horaInicio = v
    def setHoraTermino(self, v): self.__horaTermino = v
    def setDescripTareas(self, v): self.__descripTareas = v
    def setIdEmple(self, v): self.__idEmple = v
    def setIdProyecto(self, v): self.__idProyecto = v