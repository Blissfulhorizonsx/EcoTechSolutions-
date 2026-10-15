from conex import conn
import traceback

class DaoInforme:
    def __init__(self) -> None:
        try:
            self.__conn = conn.Conex("localhost", "root", "", "ecotech_bd") # cambiar bd nombre
        except Exception as ex:
            print(ex)

    def getConex(self) -> conn.Conex:
        return self.__conn

    def listarInformes(self) -> tuple:
        objetoConex = self.getConex()
        result = None
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute("SELECT idInforme, fchGeneracion, formato, contenido, idUsuario FROM informe")
            result = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            objetoConex.closeConex()
        return result

    def buscarInforme(self, info: object) -> dict:
        sql = "SELECT idInforme, fchGeneracion, formato, contenido, idUsuario FROM informe WHERE idInforme = %s"
        resultado = None
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getCo  nex().cursor()
            cursor.execute(sql, (info.getIdInforme(),))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            objetoConex.closeConex()
        return resultado

    def agregarInforme(self, info: object) -> str:
        sql = "INSERT INTO informe (fchGeneracion, formato, contenido, idUsuario) VALUES (%s, %s, %s, %s)"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (info.getFchGeneracion(), info.getFormato(), info.getContenido(), info.getIdUsuario()))
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

    def actualizarInforme(self, info: object) -> str:
        sql = "UPDATE informe SET fchGeneracion=%s, formato=%s, contenido=%s, idUsuario=%s WHERE idInforme=%s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (info.getFchGeneracion(), info.getFormato(), info.getContenido(), info.getIdUsuario(), info.getIdInforme()))
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

    def eliminarInforme(self, info: object) -> str:
        sql = "DELETE FROM informe WHERE idInforme = %s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (info.getIdInforme(),))
            objetoConex.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Informe eliminado satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje