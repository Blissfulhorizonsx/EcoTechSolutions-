from modelo.proyecto import Proyecto
from dao.dao_proyecto import DaoProyecto
from seguridad.validador_seguridad import ValidadorSeguridad

class ProyectoDTO:

    def __armar(self, p) -> Proyecto:
        return Proyecto(p["nombProyecto"], p["descripProyecto"], p["fchInicio"], p["idProyecto"])

    def listarProyectos(self) -> list:
        resultado = DaoProyecto().listarProyectos()
        return [self.__armar(p) for p in resultado] if resultado is not None else []

    def buscarProyecto(self, idProyecto: int) -> Proyecto:
        r = DaoProyecto().buscarProyecto(Proyecto("", idProyecto=idProyecto))
        return self.__armar(r) if r is not None else None

    def agregarProyecto(self, nombre: str, descripcion: str, fchInicio) -> str:
        v = ValidadorSeguridad()
        if not nombre.strip():
            return "El nombre del proyecto es obligatorio"
        proy = Proyecto(v.sanitizar_entrada(nombre), v.sanitizar_entrada(descripcion), fchInicio)
        return DaoProyecto().agregarProyecto(proy)

    def actualizarProyecto(self, idProyecto: int, nombre: str, descripcion: str, fchInicio) -> str:
        v = ValidadorSeguridad()
        if not nombre.strip():
            return "El nombre del proyecto es obligatorio"
        proy = Proyecto(v.sanitizar_entrada(nombre), v.sanitizar_entrada(descripcion), fchInicio, idProyecto)
        return DaoProyecto().actualizarProyecto(proy)

    def eliminarProyecto(self, idProyecto: int) -> str:
        return DaoProyecto().eliminarProyecto(Proyecto("", idProyecto=idProyecto))