from conex import conn


class DaoEmpleado:
    def __init__(self) -> None:
        self.__conn = conn.Conex("localhost", "root", "", "ecotech")

    def getConex(self) -> conn.Conex:
        return self.__conn

    def listarEmpleados(self) -> tuple:
        objetoConex = self.getConex()
        result = None
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute("SELECT idEmple, idUsuario, nombEmplea, direccEmple, numEmple, mailEmple, fchContrato, salarioCifrado, idDepart FROM empleado")
            result = cursor.fetchall()
        except Exception:
            pass
        finally:
            objetoConex.closeConex()
        return result

    def buscarEmpleado(self, emple: object) -> dict:
        sql = "SELECT idEmple, idUsuario, nombEmplea, direccEmple, numEmple, mailEmple, fchContrato, salarioCifrado, idDepart FROM empleado WHERE idEmple = %s"
        resultado = None
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (emple.getIdEmple(),))
            resultado = cursor.fetchone()
        except Exception:
            pass
        finally:
            objetoConex.closeConex()
        return resultado

    def buscarPorUsuario(self, emp: object) -> dict:
        sql = "SELECT * FROM empleado WHERE idUsuario = %s"
        resultado = None
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (emp.getIdUsuario(),))
            resultado = cursor.fetchone()
        except Exception:
            pass
        finally:
            objetoConex.closeConex()
        return resultado

    def agregarEmpleado(self, emple: object) -> str:
        sql = "INSERT INTO empleado (idUsuario, nombEmplea, direccEmple, numEmple, mailEmple, fchContrato, salarioCifrado, idDepart) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (emple.getIdUsuario(), emple.getNombEmplea(), emple.getDireccEmple(), emple.getNumEmple(), emple.getMailEmple(), emple.getFchContrato(), emple.getSalarioCifrado(), emple.getIdDepart()))
            objetoConex.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Datos agregados satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception:
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje

    def asignarUsuarioEmpleado(self, idEmple: int, idUsuario: int) -> str:
        sql = "UPDATE empleado SET idUsuario = %s WHERE idEmple = %s"
        mensaje = ""
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (idUsuario, idEmple))
            objetoConex.getConex().commit()
            mensaje = "Usuario asignado al empleado correctamente"
        except Exception as ex:
            objetoConex.getConex().rollback()
            mensaje = f"Error al asignar el usuario: {ex}"
        finally:
            objetoConex.closeConex()
        return mensaje


    def eliminarEmpleado(self, emple: object) -> str:
        sql = "DELETE FROM empleado WHERE idEmple = %s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (emple.getIdEmple(),))
            objetoConex.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Empleado eliminado satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception:
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje

    def asignarDepartamento(self, emple: object) -> str:
        sql = "UPDATE empleado SET idDepart=%s WHERE idEmple=%s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (emple.getIdDepart(), emple.getIdEmple()))
            objetoConex.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Departamento asignado satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception:
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje