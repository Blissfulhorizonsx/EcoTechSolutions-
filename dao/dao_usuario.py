from conex import conn
import traceback

class DaoUsuario:
    def __init__(self) -> None:
        try:
            self.__conn = conn.Conex("localhost", "root", "", "ecotech_bd") # cambiar bd nombre
        except Exception as ex:
            print(ex)

    def getConex(self) -> conn.Conex:
        return self.__conn

    def listarUsuarios(self) -> tuple:
        objetoConex = self.getConex()
        result = None
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute("SELECT idUsuario, nombreUsuario, contrasenaHash, rol FROM usuario")
            result = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            objetoConex.closeConex()
        return result

    def buscarUsuario(self, user: object) -> dict:
        sql = "SELECT idUsuario, nombreUsuario, contrasenaHash, rol FROM usuario WHERE idUsuario = %s"
        resultado = None
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (user.getIdUsuario(),))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            objetoConex.closeConex()
        return resultado

    def agregarUsuario(self, user: object) -> str:
        sql = "INSERT INTO usuario (nombreUsuario, contrasenaHash, rol) VALUES (%s, %s, %s)"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (user.getNombreUsuario(), user.getContrasenaHash(), user.getRol()))
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

    def actualizarUsuario(self, user: object) -> str:
        sql = "UPDATE usuario SET nombreUsuario=%s, contrasenaHash=%s, rol=%s WHERE idUsuario=%s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (user.getNombreUsuario(), user.getContrasenaHash(), user.getRol(), user.getIdUsuario()))
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

    def eliminarUsuario(self, user: object) -> str:
        sql = "DELETE FROM usuario WHERE idUsuario = %s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (user.getIdUsuario(),))
            objetoConex.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Usuario eliminado satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje