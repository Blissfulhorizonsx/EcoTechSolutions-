from conex.conn import Conex
import traceback

class IndicadorDAO:

    def guardarIndicadores(self, lista: list) -> str:

        sql = "INSERT INTO indicadores (idUsuario, autor, codigo, fecha, valor)" \
              " VALUES (%s, %s, %s, %s, %s)" \
              " ON DUPLICATE KEY UPDATE idUsuario = VALUES(idUsuario)," \
              " autor = VALUES(autor), valor = VALUES(valor)"

        datos = [(i.getIdUsuario(), i.getAutor(), i.getCodigo(), i.getFecha(), i.getValor())
                  for i in lista]
        objetoConex = Conex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.executemany(sql, datos)
            objetoConex.getConex().commit()
            return "Guardados en la base de datos."

        except Exception:
            traceback.print_exc()
            objetoConex.getConex().rollback()
            return "Problemas al guardar, vuelve a intentarlo."
        finally:
            objetoConex.closeConex()

    def listarPorFecha(self, codigo: str, fecha) -> list:
        sql = ("SELECT idIndicador, idUsuario, autor, codigo, fecha, valor "
        "FROM indicadores WHERE codigo = %s AND fecha = %s")

        return self._consultar(sql, (codigo, fecha))

    def listarPorRango(self, codigo: str, desde, hasta) -> list:
        sql = ("SELECT idIndicador, idUsuario, autor, codigo, fecha, valor "
        "FROM indicadores WHERE codigo = %s AND fecha BETWEEN %s AND %s "
        "ORDER BY fecha")

        return self._consultar(sql, (codigo, desde, hasta))

    def _consultar(self, sql: str, parametros: tuple) -> list:
        resultado = []
        objetoConex = Conex()
        try:
            cursor = objetoConex.getConex().cursor()
            cursor.execute(sql, parametros)
            resultado = cursor.fetchall()

        except Exception:
            traceback.print_exc()
        finally:
            objetoConex.closeConex()
        return resultado