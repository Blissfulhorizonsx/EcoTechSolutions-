from modelo.empleado import Empleado
from dao.dao_empleado import DaoEmpleado
from seguridad.validador_seguridad import ValidadorSeguridad

class EmpleadoDTO:

    def __armar(self, e) -> Empleado:
        return Empleado(e["nombEmplea"], e["direccEmple"], e["numEmple"], e["mailEmple"],
                        e["fchContrato"], e["salarioCifrado"], e["idDepart"],
                        e["idUsuario"], e["idEmple"])

    def listarEmpleados(self) -> list:
        resultado = DaoEmpleado().listarEmpleados()
        return [self.__armar(e) for e in resultado] if resultado is not None else []

    def buscarEmpleado(self, idEmple: int) -> Empleado:
        r = DaoEmpleado().buscarEmpleado(Empleado("", idEmple=idEmple))
        return self.__armar(r) if r is not None else None

    def agregarEmpleado(self, nombre, direccion, telefono, correo, fchContrato,
                        salario, idDepart=None, idUsuario=None) -> str:
        v = ValidadorSeguridad()
        cifrado = v.cifrar_dato_sensible(str(salario))
        emp = Empleado(v.sanitizar_entrada(nombre), v.sanitizar_entrada(direccion),
                       telefono, correo, fchContrato, cifrado, idDepart, idUsuario)
        return DaoEmpleado().agregarEmpleado(emp)

    def actualizarEmpleado(self, idEmple, nombre, direccion, telefono, correo,
                           fchContrato, salario, idDepart=None) -> str:
        cifrado = ValidadorSeguridad().cifrar_dato_sensible(str(salario))
        emp = Empleado(nombre, direccion, telefono, correo, fchContrato, cifrado, idDepart, idEmple=idEmple)
        return DaoEmpleado().actualizarEmpleado(emp)

    def asignarDepartamento(self, idEmple: int, idDepart: int) -> str:
        return DaoEmpleado().asignarDepartamento(Empleado("", idDepart=idDepart, idEmple=idEmple))

    def eliminarEmpleado(self, idEmple: int) -> str:
        return DaoEmpleado().eliminarEmpleado(Empleado("", idEmple=idEmple))