from conex import conn
import traceback

class DaoEmpleado:
    def __init__(self) -> None:
        try:
            self.__conn = conn.Conex("localhost", "root", "", "ecotech_bd") # Cambiar por bd
        except Exception as ex:
            print(ex)

    def getConex(self) -> conn.Conex:
        return self.__conn

    def listarEmpleados(self) -> tuple:
        objetoConex = self.getConex()
        result = None
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute("SELECT idEmple, idUsuario, nombEmplea, direccEmple, numEmple, mailEmple, fchContrato, salarioCifrado, idDepart FROM empleado")
            result = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
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
        except Exception as ex:
            print(traceback.print_exc())
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
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje

    def actualizarEmpleado(self, emple: object) -> str:
        sql = "UPDATE empleado SET idUsuario=%s, nombEmplea=%s, direccEmple=%s, numEmple=%s, mailEmple=%s, fchContrato=%s, salarioCifrado=%s, idDepart=%s WHERE idEmple=%s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (emple.getIdUsuario(), emple.getNombEmplea(), emple.getDireccEmple(), emple.getNumEmple(), emple.getMailEmple(), emple.getFchContrato(), emple.getSalarioCifrado(), emple.getIdDepart(), emple.getIdEmple()))
            objetoConex.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Datos modificados satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
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
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje