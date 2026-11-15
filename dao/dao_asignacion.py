from conex import conn


class DaoAsignacion:
    def __init__(self) -> None:
        self.__conn = conn.Conex("localhost", "root", "", "ecotech")

    def getConex(self) -> conn.Conex:
        return self.__conn

    def listarAsignaciones(self) -> tuple:
        objetoConex = self.getConex()
        result = None
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute("SELECT idAsign, fechaAsignacion, idEmple, idProyecto FROM asignacion")
            result = cursor.fetchall()
        except Exception:
            pass
        finally:
            objetoConex.closeConex()
        return result

    def buscarAsignacion(self, asign: object) -> dict:
        sql = "SELECT idAsign, fechaAsignacion, idEmple, idProyecto FROM asignacion WHERE idAsign = %s"
        resultado = None
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (asign.getIdAsign(),))
            resultado = cursor.fetchone()
        except Exception:
            pass
        finally:
            objetoConex.closeConex()
        return resultado

    def agregarAsignacion(self, asign: object) -> str:
        sql = "INSERT INTO asignacion (fechaAsignacion, idEmple, idProyecto) VALUES (%s, %s, %s)"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (asign.getFechaAsignacion(), asign.getIdEmple(), asign.getIdProyecto()))
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

    def actualizarAsignacion(self, asign: object) -> str:
        sql = "UPDATE asignacion SET fechaAsignacion=%s, idEmple=%s, idProyecto=%s WHERE idAsign=%s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (asign.getFechaAsignacion(), asign.getIdEmple(), asign.getIdProyecto(), asign.getIdAsign()))
            objetoConex.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Datos modificados satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception:
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje

    def eliminarAsignacion(self, asign: object) -> str:
        sql = "DELETE FROM asignacion WHERE idEmple = %s AND idProyecto = %s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (asign.getIdEmple(), asign.getIdProyecto()))
            objetoConex.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Asignación eliminada satisfactoriamente"
            else:
                mensaje = "No se encontraron registros para eliminar"
        except Exception:
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje

    def listarPorEmpleado(self, asign: object) -> tuple:
        sql = "SELECT idAsign, fechaAsignacion, idEmple, idProyecto FROM asignacion WHERE idEmple = %s"
        resultado = None
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (asign.getIdEmple(),))
            resultado = cursor.fetchall()
        except Exception:
            pass
        finally:
            objetoConex.closeConex()
        return resultado

    def listarPorProyecto(self, asign: object) -> tuple:
        sql = "SELECT idAsign, fechaAsignacion, idEmple, idProyecto FROM asignacion WHERE idProyecto = %s"
        resultado = None
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (asign.getIdProyecto(),))
            resultado = cursor.fetchall()
        except Exception:
            pass
        finally:
            objetoConex.closeConex()
        return resultado