import re
from datetime import datetime

from controlador.dto_departamento import DepartamentoDTO
from controlador.dto_empleado import EmpleadoDTO
from controlador.dto_usuario import UsuarioDTO
from controlador.dto_proyecto import ProyectoDTO
from controlador.dto_registrotiempo import RegistroTiempoDTO
from controlador.dto_informe import InformeDTO

# ==========================================
# 1. FUNCIONES AUXILIARES DE ENTRADA Y FORMATO
# ==========================================

def solicitar_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def solicitar_flotante(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido (ej. 7.5).")

def solicitar_texto(mensaje: str, min_len: int = 1) -> str:
    while True:
        valor = input(mensaje).strip()
        if len(valor) >= min_len:
            return valor
        print(f"Error: El campo debe contener al menos {min_len} caracter(es).")

def solicitar_fecha(mensaje: str) -> str:
    while True:
        fec = input(mensaje).strip()
        try:
            datetime.strptime(fec, "%Y-%m-%d")
            return fec
        except ValueError:
            print("Error: Fecha inválida. Utilice el formato YYYY-MM-DD.")

def solicitar_confirmacion(mensaje: str) -> bool:
    while True:
        resp = input(f"{mensaje} (S/N): ").strip().upper()
        if resp in ["S", "Y"]:
            return True
        if resp in ["N"]:
            return False
        print("Opción inválida. Ingrese S para confirmar o N para cancelar.")


# ==========================================
# 2. VALIDACIONES DE REGLAS DE NEGOCIO
# ==========================================

def validar_correo(correo: str) -> bool:
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, correo))

def validar_horas_trabajo(horas: float) -> bool:
    if 0.5 <= horas <= 24.0:
        return True
    print("Error: Las horas registradas deben estar entre 0.5 y 24.0 horas.")
    return False

def validar_formato_informe(formato: str) -> bool:
    formatos_valida = ["PDF", "CSV", "EXCEL", "TXT"]
    return formato.upper() in formatos_valida


# ==========================================
# 3. INTERFACES DE VALIDACIÓN Y FLUJO
# ==========================================

def validate_crear_departamento():
    print("\n------------------------------")
    print(" Crear Departamento ")
    print("------------------------------")
    nombre = solicitar_texto("Nombre del Departamento: ", min_len=3)
    gerente = input("Nombre del Gerente (Opcional): ").strip()
    
    mensaje = DepartamentoDTO().agregarDepartamento(nombre, gerente)
    print(f"-> {mensaje}")

def validate_agregar_empleado_dept():
    print("\n------------------------------")
    print(" Agregar Empleado a Depto ")
    print("------------------------------")
    id_emp = solicitar_entero("ID Empleado: ")
    id_dept = solicitar_entero("ID Departamento: ")
    
    mensaje = EmpleadoDTO().asignarDepartamento(id_emp, id_dept)
    print(f"-> {mensaje}")

def validate_crear_empleado():
    print("\n------------------------------")
    print(" Registrar Empleado ")
    print("------------------------------")
    nombre = solicitar_texto("Nombre Completo: ", min_len=3)
    direccion = solicitar_texto("Dirección: ")
    telefono = solicitar_texto("Teléfono: ")
    
    while True:
        correo = solicitar_texto("Correo electrónico: ")
        if validar_correo(correo):
            break
        print("Error: Correo no válido. Inténtelo de nuevo.")
        
    fecha_inicio = solicitar_fecha("Fecha inicio contrato (YYYY-MM-DD): ")
    salario_bruto = solicitar_flotante("Salario bruto: ")
    id_dept = solicitar_entero("ID Departamento (o 0 si no tiene): ")
    id_usuario = solicitar_entero("ID Usuario asociado (o 0 si no tiene): ")

    id_d = id_dept if id_dept > 0 else None
    id_u = id_usuario if id_usuario > 0 else None

    mensaje = EmpleadoDTO().agregarEmpleado(
        nombre, direccion, telefono, correo, fecha_inicio, salario_bruto, id_d, id_u
    )
    print(f"-> {mensaje}")

def validate_login():
    print("\n------------------------------")
    print(" Autenticación de Usuario ")
    print("------------------------------")
    username = solicitar_texto("Username: ")
    password = solicitar_texto("Contraseña: ")
    
    usuario = UsuarioDTO().validarLogin(username, password)
    return usuario

def validate_crear_proyecto():
    print("\n------------------------------")
    print(" Crear Proyecto ")
    print("------------------------------")
    nombre = solicitar_texto("Nombre del Proyecto: ", min_len=3)
    descripcion = solicitar_texto("Descripción: ")
    fecha_inicio = solicitar_fecha("Fecha de Inicio (YYYY-MM-DD): ")

    mensaje = ProyectoDTO().agregarProyecto(nombre, descripcion, fecha_inicio)
    print(f"-> {mensaje}")

def validate_registrar_tiempo():
    print("\n------------------------------")
    print(" Registrar Horas Trabajadas ")
    print("------------------------------")
    id_emp = solicitar_entero("ID Empleado: ")
    id_proy = solicitar_entero("ID Proyecto: ")
    fecha = solicitar_fecha("Fecha de trabajo (YYYY-MM-DD): ")
    
    hora_inicio = solicitar_texto("Hora Inicio (HH:MM): ")
    hora_termino = solicitar_texto("Hora Término (HH:MM): ")
    descripcion = solicitar_texto("Descripción de tareas realizadas: ", min_len=5)

    mensaje = RegistroTiempoDTO().registrarTiempo(
        id_emp, id_proy, fecha, hora_inicio, hora_termino, descripcion
    )
    print(f"-> {mensaje}")

def validate_generar_informe(usuario_actual):
    print("\n------------------------------")
    print(" Generar e Imprimir Informe ")
    print("------------------------------")
    if usuario_actual is None or usuario_actual.getRol() != "ADMIN":
        print("Error: Solo los administradores pueden generar informes.")
        return

    id_proy = solicitar_entero("ID del Proyecto a consultar: ")
    desde_str = solicitar_fecha("Fecha Desde (YYYY-MM-DD): ")
    hasta_str = solicitar_fecha("Fecha Hasta (YYYY-MM-DD): ")
    
    while True:
        formato = solicitar_texto("Formato de salida (PDF/CSV/EXCEL/TXT): ").upper()
        if validar_formato_informe(formato):
            break
        print("Error: Formato no soportado.")

    desde = datetime.strptime(desde_str, "%Y-%m-%d").date()
    hasta = datetime.strptime(hasta_str, "%Y-%m-%d").date()

    criterios = {"idProyecto": id_proy, "desde": desde, "hasta": hasta}

    informe = InformeDTO().generarInforme(usuario_actual, criterios, formato)
    if informe:
        print("\n=== INFORME GENERADO EXITOSAMENTE ===")
        print(informe.getContenido())
    else:
        print("-> No se pudo generar el informe. Verifique permisos o existencia del proyecto.")


# ==========================================
# 4. MENÚS Y NAVEGACIÓN PRINCIPAL
# ==========================================

def menu_principal():
    print("\n==================================")
    print("===== GESTIÓN DE TIEMPOS Y PROYECTOS =====")
    print("==================================")
    print("1. Módulo Usuarios y Empleados")
    print("2. Módulo Departamentos")
    print("3. Módulo Proyectos")
    print("4. Módulo Registro de Tiempo")
    print("5. Módulo Administrador (Informes)")
    print("6. Salir")

def valida_opc(max_opc: int) -> int:
    while True:
        opc = solicitar_entero("Seleccione una opción: ")
        if 1 <= opc <= max_opc:
            return opc
        print(f"Opción no válida. Ingrese un valor entre 1 y {max_opc}.")

def inicial(usuario_actual=None):
    while True:
        menu_principal()
        opc = valida_opc(6)
        
        if opc == 1:
            print("\n1. Login | 2. Crear Empleado")
            sub_opc = valida_opc(2)
            if sub_opc == 1: 
                usuario_actual = validate_login()
            elif sub_opc == 2: 
                validate_crear_empleado()

        elif opc == 2:
            print("\n1. Crear Depto | 2. Asignar Empleado")
            sub_opc = valida_opc(2)
            if sub_opc == 1: validate_crear_departamento()
            elif sub_opc == 2: validate_agregar_empleado_dept()

        elif opc == 3:
            validate_crear_proyecto()

        elif opc == 4:
            validate_registrar_tiempo()

        elif opc == 5:
            validate_generar_informe(usuario_actual)

        elif opc == 6:
            if solicitar_confirmacion("¿Está seguro que desea salir del sistema?"):
                print("Aplicación finalizada.")
                break

if __name__ == "__main__":
    inicial()