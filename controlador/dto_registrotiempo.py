from datetime import datetime
from modelo.registrotiempo import RegistroTiempo
from dao.dao_registrotiempo import DaoRegistroTiempo
from controlador.dto_asignacion import AsignacionDTO
from seguridad.validador_seguridad import ValidadorSeguridad


class RegistroTiempoDTO:

    def __armar(self, r) -> RegistroTiempo:
        return RegistroTiempo(r["idEmple"], r["idProyecto"], r["fchTrabajo"], r["horaInicio"],
                              r["horaTermino"], r["descripTareas"], r["idRegistro"])

    def __validarHoras(self, horaInicio: str, horaTermino: str):
        """Devuelve un mensaje de error, o None si todo está bien."""
        try:
            ini = datetime.strptime(horaInicio, "%H:%M")
            fin = datetime.strptime(horaTermino, "%H:%M")
        except ValueError:
            return "Formato de hora inválido, use HH:MM (ej: 08:30)"
        if fin <= ini:
            return "La hora de término debe ser posterior a la hora de inicio"
        return None

    def listarPorEmpleado(self, idEmple: int) -> list:
        resultado = DaoRegistroTiempo().listarPorEmpleado(RegistroTiempo(idEmple, 0))
        return [self.__armar(r) for r in resultado] if resultado is not None else []

    def listarPorProyecto(self, idProyecto: int) -> list:
        resultado = DaoRegistroTiempo().listarPorProyecto(RegistroTiempo(0, idProyecto))
        return [self.__armar(r) for r in resultado] if resultado is not None else []

    def registrarTiempo(self, idEmple: int, idProyecto: int, fchTrabajo,
                        horaInicio: str, horaTermino: str, descripTareas: str) -> str:
        error = self.__validarHoras(horaInicio, horaTermino)
        if error:
            return error
        if not AsignacionDTO().estaAsignado(idEmple, idProyecto):
            return "El empleado no está asignado a este proyecto"
        desc = ValidadorSeguridad().sanitizar_entrada(descripTareas)
        reg = RegistroTiempo(idEmple, idProyecto, fchTrabajo, horaInicio, horaTermino, desc)
        return DaoRegistroTiempo().agregarRegistro(reg)

    def editarRegistro(self, idRegistro: int, idEmple: int, idProyecto: int, fchTrabajo,
                       horaInicio: str, horaTermino: str, descripTareas: str) -> str:
        error = self.__validarHoras(horaInicio, horaTermino)
        if error:
            return error
        desc = ValidadorSeguridad().sanitizar_entrada(descripTareas)
        reg = RegistroTiempo(idEmple, idProyecto, fchTrabajo, horaInicio, horaTermino, desc, idRegistro)
        return DaoRegistroTiempo().editarRegistro(reg)

    def eliminarRegistro(self, idRegistro: int) -> str:
        return DaoRegistroTiempo().eliminarRegistro(RegistroTiempo(0, 0, idRegistro=idRegistro))