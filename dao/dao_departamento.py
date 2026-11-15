from conex.conn import Conex


class DaoDepartamento:
    def __init__(self) -> None:
        self.__conn = Conex("localhost", "root", "", "ecotech")

    def getConex(self) -> Conex:
        return self.__conn

    def listarDepartamentos(self) -> tuple:
        objetoConex = self.getConex()
        result = None
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute("SELECT idDepart, nombDepart, gerentDepart FROM departamento")
            result = cursor.fetchall()
        except Exception:
            pass
        finally:
            objetoConex.closeConex()
        return result

    def buscarDepartamento(self, depart: object) -> dict:
        sql = "SELECT idDepart, nombDepart, gerentDepart FROM departamento WHERE idDepart = %s"
        resultado = None
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (depart.getIdDepart(),))
            resultado = cursor.fetchone()
        except Exception:
            pass
        finally:
            objetoConex.closeConex()
        return resultado

    def agregarDepartamento(self, depart: object) -> str:
        sql = "INSERT INTO departamento (nombDepart, gerentDepart) VALUES (%s, %s)"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (depart.getNombDepart(), depart.getGerentDepart()))
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

    def actualizarDepartamento(self, depart: object) -> str:
        sql = "UPDATE departamento SET nombDepart=%s, gerentDepart=%s WHERE idDepart=%s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (depart.getNombDepart(), depart.getGerentDepart(), depart.getIdDepart()))
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

    def eliminarDepartamento(self, depart: object) -> str:
        sql = "DELETE FROM departamento WHERE idDepart = %s"
        objetoConex = self.getConex()
        mensaje = ""
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (depart.getIdDepart(),))
            objetoConex.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Departamento eliminado satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception:
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            objetoConex.closeConex()
        return mensaje

    def listarEmpleados(self, depart: object) -> tuple:
        sql = "SELECT idEmple, idUsuario, nombEmplea, direccEmple, numEmple, mailEmple, fchContrato, salarioCifrado, idDepart FROM empleado WHERE idDepart = %s"
        resultado = None
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, (depart.getIdDepart(),))
            resultado = cursor.fetchall()
        except Exception:
            pass
        finally:
            objetoConex.closeConex()
        return resultado