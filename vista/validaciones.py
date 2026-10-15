import re
import getpass
from datetime import datetime

from controlador.dto_departamento import DepartamentoDTO
from controlador.dto_empleado import EmpleadoDTO
from controlador.dto_usuario import UsuarioDTO
from controlador.dto_proyecto import ProyectoDTO
from controlador.dto_asignacion import AsignacionDTO
from controlador.dto_registrotiempo import RegistroTiempoDTO
from controlador.dto_informe import InformeDTO

ANCHO = 60


def banner(titulo: str, subtitulo: str = "") -> None:
    print("\n" + "=" * ANCHO)
    print(titulo.center(ANCHO))
    if subtitulo:
        print(subtitulo.center(ANCHO))
    print("=" * ANCHO)

def encabezado(titulo: str) -> None:
    print("\n" + "-" * ANCHO)
    print(f" {titulo}")
    print("-" * ANCHO)

def mostrar_menu(titulo: str, opciones: list) -> None:
    encabezado(titulo)
    for i, texto in enumerate(opciones, start=1):
        print(f"  [{i}] {texto}")
    print()

def ok(mensaje: str) -> None:
    print(f"\n  [OK] {mensaje}")

def error(mensaje: str) -> None:
    print(f"\n  [!] {mensaje}")

def resultado(mensaje: str) -> None:
    texto = str(mensaje).lower()
    if "problema" in texto or "error" in texto:
        error(mensaje)
    else:
        ok(mensaje)

def pausa() -> None:
    input("\n  Presione ENTER para continuar...")

def tabla(columnas: list, filas: list) -> None:
    """Imprime una tabla simple. columnas: ['ID','Nombre'], filas: [[1,'Ana'], ...]"""
    if not filas:
        print("  (sin resultados)")
        return
    anchos = [len(c) for c in columnas]
    for fila in filas:
        for i, celda in enumerate(fila):
            anchos[i] = max(anchos[i], len(str(celda)))
    linea = "  +" + "+".join("-" * (a + 2) for a in anchos) + "+"
    print(linea)
    print("  | " + " | ".join(c.ljust(anchos[i]) for i, c in enumerate(columnas)) + " |")
    print(linea)
    for fila in filas:
        print("  | " + " | ".join(str(c).ljust(anchos[i]) for i, c in enumerate(fila)) + " |")
    print(linea)

def solicitar_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            error("Debe ingresar un número entero válido.")

def solicitar_flotante(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            error("Debe ingresar un número válido (ej. 850000).")

def solicitar_texto(mensaje: str, min_len: int = 1) -> str:
    while True:
        valor = input(mensaje).strip()
        if len(valor) >= min_len:
            return valor
        error(f"El campo debe tener al menos {min_len} caracter(es).")

def solicitar_fecha(mensaje: str) -> str:
    while True:
        fec = input(mensaje).strip()
        try:
            datetime.strptime(fec, "%Y-%m-%d")
            return fec
        except ValueError:
            error("Fecha inválida. Use el formato AAAA-MM-DD (ej. 2026-10-15).")

def solicitar_hora(mensaje: str) -> str:
    while True:
        h = input(mensaje).strip()
        try:
            datetime.strptime(h, "%H:%M")
            return h
        except ValueError:
            error("Hora inválida. Use el formato HH:MM (ej. 08:30).")

def solicitar_confirmacion(mensaje: str) -> bool:
    while True:
        resp = input(f"  {mensaje} (S/N): ").strip().upper()
        if resp in ("S", "Y"):
            return True
        if resp == "N":
            return False
        error("Ingrese S para confirmar o N para cancelar.")

def valida_opc(max_opc: int) -> int:
    while True:
        opc = solicitar_entero("  Seleccione una opción: ")
        if 1 <= opc <= max_opc:
            return opc
        error(f"Opción no válida. Ingrese un valor entre 1 y {max_opc}.")



def validar_correo(correo: str) -> bool:
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo))

def validar_formato_informe(formato: str) -> bool:
    return formato.upper() in ["PDF", "CSV", "EXCEL", "TXT"]





def validate_login():
    encabezado("AUTENTICACIÓN")
    username = input("  Usuario    : ").strip()
    clave = getpass.getpass("  Contraseña : ")
    return UsuarioDTO().validarLogin(username, clave)



def validate_listar_empleados():
    encabezado("LISTADO DE EMPLEADOS")
    lista = EmpleadoDTO().listarEmpleados()
    tabla(["ID", "Nombre", "Correo", "Depto"],
          [[e.getIdEmple(), e.getNombEmplea(), e.getMailEmple(), e.getIdDepart() or "-"]
           for e in lista])

def validate_crear_empleado():
    encabezado("REGISTRAR EMPLEADO")
    nombre = solicitar_texto("  Nombre completo : ", min_len=3)
    direccion = solicitar_texto("  Dirección       : ")
    telefono = solicitar_texto("  Teléfono        : ")

    while True:
        correo = solicitar_texto("  Correo          : ")
        if validar_correo(correo):
            break
        error("Correo no válido. Inténtelo de nuevo.")

    fecha_inicio = solicitar_fecha("  Inicio contrato (AAAA-MM-DD): ")
    salario = solicitar_flotante("  Salario bruto   : ")
    id_dept = solicitar_entero("  ID Departamento (0 si no tiene): ")
    validate_listar_usuarios()
    id_usuario = solicitar_entero("  ID Usuario asociado (0 si no tiene): ")

    mensaje = EmpleadoDTO().agregarEmpleado(
        nombre, direccion, telefono, correo, fecha_inicio, salario,
        id_dept if id_dept > 0 else None,
        id_usuario if id_usuario > 0 else None)
    resultado(mensaje)

def validate_agregar_empleado_dept():
    encabezado("ASIGNAR EMPLEADO A DEPARTAMENTO")
    validate_listar_empleados()
    validate_listar_departamentos()
    id_emp = solicitar_entero("  ID Empleado     : ")
    id_dept = solicitar_entero("  ID Departamento : ")
    resultado(EmpleadoDTO().asignarDepartamento(id_emp, id_dept))

def validate_listar_usuarios():
    encabezado("LISTADO DE USUARIOS")
    lista = UsuarioDTO().listarUsuarios()
    tabla(["ID", "Usuario", "Rol"],
          [[u.getIdUsuario(), u.getNombreUsuario(), u.getRol()] for u in lista])

def validate_crear_usuario():
    encabezado("CREAR USUARIO")
    nombre = solicitar_texto("  Nombre de usuario : ", min_len=3)
    while True:
        clave = getpass.getpass("  Contraseña (mín. 8 caracteres): ")
        if len(clave) >= 8:
            break
        error("La contraseña debe tener al menos 8 caracteres.")
    mostrar_menu("ROL", ["EMPLEADO", "ADMIN"])
    rol = "EMPLEADO" if valida_opc(2) == 1 else "ADMIN"
    resultado(UsuarioDTO().agregarUsuario(nombre, clave, rol))



def validate_listar_departamentos():
    encabezado("LISTADO DE DEPARTAMENTOS")
    lista = DepartamentoDTO().listarDepartamentos()
    tabla(["ID", "Departamento", "Gerente"],
          [[d.getIdDepart(), d.getNombDepart(), d.getGerentDepart() or "-"] for d in lista])

def validate_crear_departamento():
    encabezado("CREAR DEPARTAMENTO")
    nombre = solicitar_texto("  Nombre del departamento : ", min_len=3)
    gerente = input("  Gerente (opcional)      : ").strip()
    resultado(DepartamentoDTO().agregarDepartamento(nombre, gerente))


def validate_listar_proyectos():
    encabezado("LISTADO DE PROYECTOS")
    lista = ProyectoDTO().listarProyectos()
    tabla(["ID", "Proyecto", "Inicio", "Descripción"],
          [[p.getIdProyecto(), p.getNombProyecto(), p.getFchInicio(), p.getDescripProyecto()]
           for p in lista])

def validate_crear_proyecto():
    encabezado("CREAR PROYECTO")
    nombre = solicitar_texto("  Nombre del proyecto : ", min_len=3)
    descripcion = solicitar_texto("  Descripción         : ")
    fecha_inicio = solicitar_fecha("  Inicio (AAAA-MM-DD) : ")
    resultado(ProyectoDTO().agregarProyecto(nombre, descripcion, fecha_inicio))

def validate_asignar_proyecto():
    encabezado("ASIGNAR EMPLEADO A PROYECTO")
    validate_listar_empleados()
    validate_listar_proyectos()
    id_emp = solicitar_entero("  ID Empleado : ")
    id_proy = solicitar_entero("  ID Proyecto : ")
    resultado(AsignacionDTO().asignar(id_emp, id_proy))

def __obtener_id_empleado(usuario):
    """Empleado: usa su propio id. Admin: elige el empleado."""
    if usuario.getRol() == "ADMIN":
        return solicitar_entero("  ID Empleado : ")
    emp = EmpleadoDTO().buscarPorUsuario(usuario.getIdUsuario())
    if emp is None:
        error("Tu usuario no tiene un empleado asociado. Contacta al administrador.")
        return None
    return emp.getIdEmple()

def validate_registrar_tiempo(usuario):
    encabezado("REGISTRAR HORAS TRABAJADAS")
    id_emp = __obtener_id_empleado(usuario)
    if id_emp is None:
        return
    id_proy = solicitar_entero("  ID Proyecto             : ")
    fecha = solicitar_fecha("  Fecha (AAAA-MM-DD)      : ")
    hora_inicio = solicitar_hora("  Hora de inicio          : ")
    hora_termino = solicitar_hora("  Hora de término         : ")
    descripcion = solicitar_texto("  Tareas realizadas       : ", min_len=5)
    resultado(RegistroTiempoDTO().registrarTiempo(
        id_emp, id_proy, fecha, hora_inicio, hora_termino, descripcion))

def validate_ver_registros(usuario):
    encabezado("MIS REGISTROS DE TIEMPO")
    id_emp = __obtener_id_empleado(usuario)
    if id_emp is None:
        return
    lista = RegistroTiempoDTO().listarPorEmpleado(id_emp)
    tabla(["Fecha", "Proyecto", "Horas", "Tareas"],
          [[r.getFchTrabajo(), r.getIdProyecto(), r.calcularHoras(), r.getDescripTareas()]
           for r in lista])



def validate_generar_informe(usuario_actual):
    encabezado("GENERAR INFORME")
    if usuario_actual is None or usuario_actual.getRol() != "ADMIN":
        error("Solo los administradores pueden generar informes.")
        return
    
    proyectos = ProyectoDTO().listarProyectos()
    if not proyectos:
        error("No hay proyectos registrados. Cree uno primero.")
        return
    validate_listar_proyectos()
    id_proy = solicitar_entero("  ID del proyecto         : ")
    desde = datetime.strptime(solicitar_fecha("  Desde (AAAA-MM-DD)      : "), "%Y-%m-%d").date()
    hasta = datetime.strptime(solicitar_fecha("  Hasta (AAAA-MM-DD)      : "), "%Y-%m-%d").date()

    while True:
        formato = solicitar_texto("  Formato (PDF/CSV/EXCEL/TXT): ").upper()
        if validar_formato_informe(formato):
            break
        error("Formato no soportado.")

    criterios = {"idProyecto": id_proy, "desde": desde, "hasta": hasta}
    informe = InformeDTO().generarInforme(usuario_actual, criterios, formato)
    if informe:
        banner("INFORME GENERADO")
        print(informe.getContenido())
        print("=" * ANCHO)
    else:
        error("No se pudo generar el informe. Verifique permisos o que el proyecto exista.")


def menu_empleados():
    while True:
        mostrar_menu("EMPLEADOS", ["Listar empleados", "Registrar empleado",
                                   "Crear usuario de acceso", "Volver"])
        opc = valida_opc(4)
        if opc == 1: validate_listar_empleados()
        elif opc == 2: validate_crear_empleado()
        elif opc == 3: validate_crear_usuario()
        else: return
        pausa()

def menu_departamentos():
    while True:
        mostrar_menu("DEPARTAMENTOS", ["Listar departamentos", "Crear departamento",
                                       "Asignar empleado a departamento", "Volver"])
        opc = valida_opc(4)
        if opc == 1: validate_listar_departamentos()
        elif opc == 2: validate_crear_departamento()
        elif opc == 3: validate_agregar_empleado_dept()
        else: return
        pausa()

def menu_proyectos():
    while True:
        mostrar_menu("PROYECTOS", ["Listar proyectos", "Crear proyecto",
                                   "Asignar empleado a proyecto", "Volver"])
        opc = valida_opc(4)
        if opc == 1: validate_listar_proyectos()
        elif opc == 2: validate_crear_proyecto()
        elif opc == 3: validate_asignar_proyecto()
        else: return
        pausa()

def menu_tiempo(usuario):
    while True:
        mostrar_menu("REGISTRO DE TIEMPO", ["Registrar horas", "Ver registros", "Volver"])
        opc = valida_opc(3)
        if opc == 1: validate_registrar_tiempo(usuario)
        elif opc == 2: validate_ver_registros(usuario)
        else: return
        pausa()

def inicial(usuario) -> None:
    es_admin = usuario.getRol() == "ADMIN"

    while True:
        if es_admin:
            opciones = ["Empleados y usuarios", "Departamentos", "Proyectos",
                        "Registro de tiempo", "Informes", "Salir"]
        else:
            opciones = ["Registro de tiempo", "Salir"]

        mostrar_menu(f"MENÚ PRINCIPAL  |  {usuario.getNombreUsuario()} ({usuario.getRol()})", opciones)
        elegida = opciones[valida_opc(len(opciones)) - 1]

        if elegida == "Empleados y usuarios":
            menu_empleados()
        elif elegida == "Departamentos":
            menu_departamentos()
        elif elegida == "Proyectos":
            menu_proyectos()
        elif elegida == "Registro de tiempo":
            menu_tiempo(usuario)
        elif elegida == "Informes":
            validate_generar_informe(usuario)
            pausa()
        elif elegida == "Salir":
            if solicitar_confirmacion("¿Está seguro que desea salir del sistema?"):
                banner("SESIÓN FINALIZADA", "¡Hasta pronto!")
                break