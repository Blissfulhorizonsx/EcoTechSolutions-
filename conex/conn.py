import pymysql as conn


class Conex:

    def __init__(self, host: str = "localhost", user: str = "root",
                 passwd: str = "", database: str = "ecotech") -> None:
        self.__myconn = None
        try:
            self.__myconn = conn.connect(host=host, user=user, passwd=passwd,
                                         database=database,
                                         cursorclass=conn.cursors.DictCursor)
        except Exception as ex:
            print("Error de conexión:", ex)

    def closeConex(self) -> None:
        if self.__myconn is not None:
            self.__myconn.close()

    def getConex(self) -> conn.Connection:
        return self.__myconn