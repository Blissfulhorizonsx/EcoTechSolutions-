from conex import conn
import traceback

class DaoProyecto:
    def __init__(self) -> None:
        try:
            self.__conn = conn.Conex("localhost", "root", "", "ecotech_bd") # cambiar bd 
        except Exception as ex:
            print(ex)

    def getConex(self) -> conn.Conex:
        return self.__conn

    def listarProyectos(self) -> tuple:
        objetoConex = self.getConex()
        result = None
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute("SELECT idProyecto, nombProyecto, descripProyecto, fchInicio FROM proyecto")
            result = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            objetoConex.closeConex()
        return result

    def buscarProyecto(self, proy: object) -> dict:
        sql = "SELECT idProyecto, nombProyecto, descripProyecto, fchInicio FROM proyecto WHERE idProyecto = %s"
        resultado = None
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (proy.getIdProyecto(),))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            objetoConex.closeConex()
        return resultado

    def agregarProyecto(self, proy: object) -> str:
        sql = "INSERT INTO proyecto (nombProyecto, descripProyecto, fchInicio) VALUES (%s, %s, %s)"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (proy.getNombProyecto(), proy.getDescripProyecto(), proy.getFchInicio()))
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

    def actualizarProyecto(self, proy: object) -> str:
        sql = "UPDATE proyecto SET nombProyecto=%s, descripProyecto=%s, fchInicio=%s WHERE idProyecto=%s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (proy.getNombProyecto(), proy.getDescripProyecto(), proy.getFchInicio(), proy.getIdProyecto()))
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

    def eliminarProyecto(self, proy: object) -> str:
        sql = "DELETE FROM proyecto WHERE idProyecto = %s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (proy.getIdProyecto(),))
            objetoConex.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Proyecto eliminado satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje