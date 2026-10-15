from datetime import date
from modelo.asignacion import Asignacion
from dao.dao_asignacion import DaoAsignacion


class AsignacionDTO:

    def __armar(self, a) -> Asignacion:
        return Asignacion(a["idEmple"], a["idProyecto"], a["fechaAsignacion"], a["idAsign"])

    def estaAsignado(self, idEmple: int, idProyecto: int) -> bool:
        r = DaoAsignacion().buscarAsignacion(Asignacion(idEmple, idProyecto))
        return r is not None

    def asignar(self, idEmple: int, idProyecto: int) -> str:
        if self.estaAsignado(idEmple, idProyecto):
            return "El empleado ya está asignado a este proyecto"
        asig = Asignacion(idEmple, idProyecto, date.today())
        return DaoAsignacion().agregarAsignacion(asig)

    def desasignar(self, idEmple: int, idProyecto: int) -> str:
        return DaoAsignacion().eliminarAsignacion(Asignacion(idEmple, idProyecto))

    def listarPorEmpleado(self, idEmple: int) -> list:
        resultado = DaoAsignacion().listarPorEmpleado(Asignacion(idEmple, 0))
        return [self.__armar(a) for a in resultado] if resultado is not None else []

    def listarPorProyecto(self, idProyecto: int) -> list:
        resultado = DaoAsignacion().listarPorProyecto(Asignacion(0, idProyecto))
        return [self.__armar(a) for a in resultado] if resultado is not None else []