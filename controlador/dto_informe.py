from datetime import datetime
from modelo.informe import Informe
from dao.dao_informe import DaoInforme
from controlador.dto_registrotiempo import RegistroTiempoDTO
from controlador.dto_empleado import EmpleadoDTO
from controlador.dto_proyecto import ProyectoDTO


class InformeDTO:

    def __armar(self, i) -> Informe:
        return Informe(i["idUsuario"], i["fchGeneracion"], i["formato"], i["contenido"], i["idInforme"])

    def listarPorUsuario(self, idUsuario: int) -> list:
        resultado = DaoInforme().listarPorUsuario(Informe(idUsuario))
        return [self.__armar(i) for i in resultado] if resultado is not None else []

    def buscarInforme(self, idInforme: int) -> Informe:
        r = DaoInforme().buscarInforme(Informe(0, idInforme=idInforme))
        return self.__armar(r) if r is not None else None

    def generarInforme(self, usuario, criterios: dict, formato: str = "TXT") -> Informe:
        """usuario: objeto Usuario que lo pide.
        criterios: {"idProyecto": int, "desde": date, "hasta": date}"""
        if usuario.getRol() != "ADMIN":
            return None

        proyecto = ProyectoDTO().buscarProyecto(criterios["idProyecto"])
        if proyecto is None:
            return None

        # minutos totales por empleado, dentro del rango de fechas
        minutos = {}
        for r in RegistroTiempoDTO().listarPorProyecto(criterios["idProyecto"]):
            if criterios["desde"] <= r.getFchTrabajo() <= criterios["hasta"]:
                h, m = r.calcularHoras().split(":")
                minutos[r.getIdEmple()] = minutos.get(r.getIdEmple(), 0) + int(h) * 60 + int(m)

        lineas = ["Informe de horas - Proyecto: {0}".format(proyecto.getNombProyecto()),
                  "Periodo: {0} a {1}".format(criterios["desde"], criterios["hasta"]), ""]
        for idEmple, total in minutos.items():
            emp = EmpleadoDTO().buscarEmpleado(idEmple)
            nombre = emp.getNombEmplea() if emp else "Empleado {0}".format(idEmple)
            lineas.append("{0}: {1:02d}:{2:02d}".format(nombre, total // 60, total % 60))
        if not minutos:
            lineas.append("Sin registros en el periodo")

        informe = Informe(usuario.getIdUsuario(), datetime.now().date(), formato, "\n".join(lineas))
        DaoInforme().agregarInforme(informe)
        return informe

    def eliminarInforme(self, idInforme: int) -> str:
        return DaoInforme().eliminarInforme(Informe(0, idInforme=idInforme))