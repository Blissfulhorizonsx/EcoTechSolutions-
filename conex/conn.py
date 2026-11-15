import pymysql as conn


class Conex:

    def __init__(self, host: str = "localhost", user: str = "root",
                 passwd: str = "", database: str = "ecotech") -> None:
        self.__myconn = None
        try:
            self.__myconn = conn.connect(host=host, user=user, passwd=passwd,
                                         database=database,
                                         cursorclass=conn.cursors.DictCursor)
        except conn.MySQLError as ex:
            codigo_error = ex.args[0] if ex.args else 0
            if codigo_error == 1045:
                mensaje_error = "Se rechazó el usuario o la contraseña de la base datos, contactese con un administrador."
            elif codigo_error == 1049:
                mensaje_error = "La base de datos no existe."
            elif codigo_error == 2003:
                mensaje_error = "No se pudo conectar con la base de datos, verifique la conexión."
            else:
                mensaje_error = "No se pudo establecer conexión con la base de datos."

            raise ConnectionError(mensaje_error)

    def closeConex(self) -> None:
        if self.__myconn is not None:
            self.__myconn.close()

    def getConex(self) -> conn.Connection:
        return self.__myconn