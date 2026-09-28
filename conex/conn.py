import pymysql as conn

class Conex:

    def __init__(self,  host: str, user: str, passwd: str, database: str)-> None:
        try:
            self.__myconn = conn.connect(host=host, user=user, passwd=passwd, database=database,cursorclass=conn.cursors.DictCursor,)

        except Exception as ex:
            print(ex)
            self.__myconn.rollback()
            return None

    def closeConex(self) -> None:
        self.__myconn.close()

    def getConex(self)-> conn.Connection:
        return self.__myconn
