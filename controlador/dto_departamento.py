from modelo.departamento import Departamento
from modelo.proyecto import Empleado
from dao.dao_departamento import DaoDepartamento
from seguridad.validador_seguridad import ValidadorSeguridad

class DepartamentoDTO:

    def __armar(self, d) -> Departamento:
        return Departamento(d["nombDepart"], d["gerentDepart"], d["idDepart"])

    def listarDepartamentos(self) -> list:
        resultado = DaoDepartamento().listarDepartamentos()
        return [self.__armar(d) for d in resultado] if resultado is not None else []

    def buscarDepartamento(self, idDepart: int) -> Departamento:
        r = DaoDepartamento().buscarDepartamento(Departamento("", idDepart=idDepart))
        return self.__armar(r) if r is not None else None

    def agregarDepartamento(self, nombre: str, gerente: str = "") -> str:
        v = ValidadorSeguridad()
        if not nombre.strip():
            return "El nombre del departamento es obligatorio"
        dep = Departamento(v.sanitizar_entrada(nombre), v.sanitizar_entrada(gerente))
        return DaoDepartamento().agregarDepartamento(dep)

    def actualizarDepartamento(self, idDepart: int, nombre: str, gerente: str = "") -> str:
        v = ValidadorSeguridad()
        if not nombre.strip():
            return "El nombre del departamento es obligatorio"
        dep = Departamento(v.sanitizar_entrada(nombre), v.sanitizar_entrada(gerente), idDepart)
        return DaoDepartamento().actualizarDepartamento(dep)

    def eliminarDepartamento(self, idDepart: int) -> str:
        return DaoDepartamento().eliminarDepartamento(Departamento("", idDepart=idDepart))

    def listarEmpleadosDeDepartamento(self, idDepart: int) -> list:
        resultado = DaoDepartamento().listarEmpleados(Departamento("", idDepart=idDepart))
        lista = []
        if resultado is not None:
            for e in resultado:
                lista.append(Empleado(e["nombEmplea"], e["direccEmple"], e["numEmple"],
                                      e["mailEmple"], e["fchContrato"], e["salarioCifrado"],
                                      e["idDepart"], e["idUsuario"], e["idEmple"]))
        return lista