from datetime import timedelta
from modelo.indicador import indicador
from dao.dao_indicador import IndicadorDAO
from controlador.consultar_indicadores import consultar_indicador, codigos


class IndicadorDTO:
    rol_permitIdo = "RRHH"
    limite_dias = 31 

    def __validarAcceso(self, usuario) -> None:
        if usuario is None or usuario.getRol() != self.rol_permitido:
            raise PermissionError("Solo encargado de recursos humanos puede acceder a los indicadores.")
    
    def __codigos(self, codigo) -> list:
        return codigos if codigo is None else [codigo]

    def __armar(self, r) -> indicador:
        return indicador(r["codigo"], r["fecha"], float(r["valor"]), r["autor"],
                         r["idUsuario"], r["idIndicador"])

    def actualizar(self, usuario, codigo: str = None, fecha: str = None) -> str:
        self.__validarAcceso(usuario)
        mensajes = []
        for cod in self.__codigos(codigo):
            try:
                datos = consultar_indicador(cod, fecha)
            except ConnectionError as ex:
                mensajes.append(f"{cod.upper()}: no se puede consultar ninguna API({ex})")
                continue
            if not datos["serie"]:
                mensajes.append(f"{cod.upper()}: sin valor para esa fecha (fin de semana o feriado)")
                continue
            lista = []
            for s in datos["serie"]:
                lista.append(indicador(cod, s["fecha"], s["valor"], datos["autor"], usuario.getIdUsuario()))
            resultado = IndicadorDAO().guardarIndicadores(lista)
            mensajes.append(f"{cod.upper()}: {len(lista)} valores desde {datos['autor']}. {resultado}")
        return "\n".join(mensajes)

    def consultarPorFecha(self, usuario, codigo: str, fecha) -> list:
        self.__validarAcceso(usuario)
        resultado = []
        for cod in self.__codigos(codigo):
            filas = IndicadorDAO().listarPorFecha(cod, fecha)
            if not filas:
                self.actualizar(usuario, cod, fecha.strftime("%d-%m-%Y"))
                filas = IndicadorDAO().listarPorFecha(cod, fecha)
            for f in filas or []:
                resultado.append(self.__armar(f))
        return resultado

    def consultarPorRango(self, usuario, codigo: str, desde, hasta) -> list:
        self.__validarAcceso(usuario)
        if hasta < desde:
            return []
        resultado = []
        for cod in self.__codigos(codigo):
            filas = IndicadorDAO().listarPorRango(cod,desde,hasta)
            if not filas:
                self.actualizar(usuario, cod)
                filas = IndicadorDAO().listarPorRango(cod, desde, hasta)
            if not filas and (hasta - desde).days < self.limite_dias:
                dia = desde
                while dia <= hasta:
                    self.actualizar(usuario, cod, dia.strftime("%d-%m-%Y"))
                    dia = dia + timedelta(days=1)
                filas = IndicadorDAO().listarPorRango(cod, desde, hasta)
            for f in filas or []:
                resultado.append(self.__armar(f))
        return resultado