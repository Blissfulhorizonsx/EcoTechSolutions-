from conex import conn
import traceback

class DaoRegistroTiempo:
    def __init__(self) -> None:
        try:
            self.__conn = conn.Conex("localhost", "root", "", "ecotech_bd") # cambiar nombre bd
        except Exception as ex:
            print(ex)

    def getConex(self) -> conn.Conex:
        return self.__conn

    def listarRegistrosTiempo(self) -> tuple:
        objetoConex = self.getConex()
        result = None
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute("SELECT idRegistro, fchTrabajo, horaInicio, horaTermino, descripTareas, idEmpleado, idProyecto FROM registroTiempo")
            result = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            objetoConex.closeConex()
        return result

    def buscarRegistroTiempo(self, reg: object) -> dict:
        sql = "SELECT idRegistro, fchTrabajo, horaInicio, horaTermino, descripTareas, idEmpleado, idProyecto FROM registroTiempo WHERE idRegistro = %s"
        resultado = None
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (reg.getIdRegistro(),))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            objetoConex.closeConex()
        return resultado

    def agregarRegistroTiempo(self, reg: object) -> str:
        sql = "INSERT INTO registroTiempo (fchTrabajo, horaInicio, horaTermino, descripTareas, idEmpleado, idProyecto) VALUES (%s, %s, %s, %s, %s, %s)"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (reg.getFchTrabajo(), reg.getHoraInicio(), reg.getHoraTermino(), reg.getDescripTareas(), reg.getIdEmpleado(), reg.getIdProyecto()))
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

    def actualizarRegistroTiempo(self, reg: object) -> str:
        sql = "UPDATE registroTiempo SET fchTrabajo=%s, horaInicio=%s, horaTermino=%s, descripTareas=%s, idEmpleado=%s, idProyecto=%s WHERE idRegistro=%s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (reg.getFchTrabajo(), reg.getHoraInicio(), reg.getHoraTermino(), reg.getDescripTareas(), reg.getIdEmpleado(), reg.getIdProyecto(), reg.getIdRegistro()))
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

    def eliminarRegistroTiempo(self, reg: object) -> str:
        sql = "DELETE FROM registroTiempo WHERE idRegistro = %s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (reg.getIdRegistro(),))
            objetoConex.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Registro de tiempo eliminado satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje