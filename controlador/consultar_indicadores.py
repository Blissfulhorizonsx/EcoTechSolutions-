import requests
from datetime import datetime


base_url_findic = "https://findic.cl/api"
base_url = "https://mindicador.cl/api"
fuentes = [("findic.cl", base_url_findic), ("mindicador.cl", base_url)]
codigos = ["uf", "dolar", "euro", "utm"]

def consultar_api(base_url, codigo, fecha=None):
    url = f"{base_url}/{codigo}/{fecha}" if fecha else f"{base_url}/{codigo}"
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()
    return respuesta.json()

def limpiar_serie(serie):
    lista = []
    for item in serie:
        try:
            fecha = datetime.strptime(str(item["fecha"])[:10], "%Y-%m-%d").date()
            lista.append({"fecha": fecha, "valor": float(item["valor"])})
        except (KeyError,ValueError,TypeError):
            continue
    return lista


def consultar_indicador(codigo, fecha=None):
    errores = []
    respondio = None
    for autor, base_url in fuentes:
        try:
            datos = consultar_api(base_url, codigo, fecha)
            serie = limpiar_serie(datos.get("serie", []))

            if serie:
                return {"autor": autor, "codigo": codigo, "serie": serie}
            respondio = autor

        except (requests.RequestException, ValueError, AttributeError) as ex:
            errores.append(f"{autor}: {ex}")
    if respondio is not None:
        return {"autor": respondio, "codigo": codigo, "serie": []}
    raise ConnectionError("; ".join(errores))

