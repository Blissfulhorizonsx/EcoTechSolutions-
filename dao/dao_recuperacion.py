from conex.conn import Conex
import traceback


class DaoRecuperacion:
    """Crear una instancia nueva por cada llamada, igual que el resto de los DAO
    (cada método cierra la conexión al terminar)."""

    def __init__(self) -> None:
        try:
            self.__conn = Conex("localhost", "root", "", "ecotech")
        except Exception as ex:
            print(ex)

    def getConex(self) -> Conex:
        return self.__conn

    def __escribir(self, sql: str, parametros: tuple):
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, parametros)
            objetoConex.getConex().commit()
            return cursor.rowcount
        except Exception:
            traceback.print_exc()
            return None
        finally:
            objetoConex.closeConex()

    def __leer(self, sql: str, parametros: tuple):
        objetoConex = self.getConex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, parametros)
            return cursor.fetchone()
        except Exception:
            traceback.print_exc()
            return None
        finally:
            objetoConex.closeConex()

    def invalidarPendientes(self, idUsuario: int) -> None:
        self.__escribir("UPDATE recuperacion_clave SET usado = 1 "
                        "WHERE idUsuario = %s AND usado = 0", (idUsuario,))

    def crear(self, idUsuario: int, codigoHash: str, minutos: int) -> bool:
        sql = ("INSERT INTO recuperacion_clave (idUsuario, codigoHash, expira) "
               "VALUES (%s, %s, DATE_ADD(NOW(), INTERVAL %s MINUTE))")
        return self.__escribir(sql, (idUsuario, codigoHash, minutos)) == 1

    def buscarVigente(self, idUsuario: int) -> dict:
        sql = ("SELECT idRecuperacion, codigoHash, intentos FROM recuperacion_clave "
               "WHERE idUsuario = %s AND usado = 0 AND expira > NOW() "
               "ORDER BY idRecuperacion DESC LIMIT 1")
        return self.__leer(sql, (idUsuario,))

    def solicitudesRecientes(self, idUsuario: int, segundos: int) -> int:
        sql = ("SELECT COUNT(*) AS total FROM recuperacion_clave "
               "WHERE idUsuario = %s AND creado > DATE_SUB(NOW(), INTERVAL %s SECOND)")
        r = self.__leer(sql, (idUsuario, segundos))
        return r["total"] if r else 0

    def sumarIntento(self, idRecuperacion: int) -> None:
        self.__escribir("UPDATE recuperacion_clave SET intentos = intentos + 1 "
                        "WHERE idRecuperacion = %s", (idRecuperacion,))

    def marcarUsado(self, idRecuperacion: int) -> None:
        self.__escribir("UPDATE recuperacion_clave SET usado = 1 "
                        "WHERE idRecuperacion = %s", (idRecuperacion,))