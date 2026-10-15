import re
from datetime import datetime

# ==========================================
# 1. FUNCIONES AUXILIARES DE ENTRADA Y FORMATO
# ==========================================

def solicitar_entero(mensaje: str) -> int:
    """Garantiza el ingreso de un número entero."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def solicitar_flotante(mensaje: str) -> float:
    """Garantiza el ingreso de un número decimal/float."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido (ej. 7.5).")

def solicitar_texto(mensaje: str, min_len: int = 1) -> str:
    """Solicita un texto y asegura un largo mínimo."""
    while True:
        valor = input(mensaje).strip()
        if len(valor) >= min_len:
            return valor
        print(f"Error: El campo debe contener al menos {min_len} caracter(es).")

def solicitar_fecha(mensaje: str) -> str:
    """Garantiza una fecha con formato YYYY-MM-DD."""
    while True:
        fec = input(mensaje).strip()
        try:
            datetime.strptime(fec, "%Y-%m-%d")
            return fec
        except ValueError:
            print("Error: Fecha inválida. Utilice el formato YYYY-MM-DD.")

def solicitar_confirmacion(mensaje: str) -> bool:
    """Solicita confirmación Y/N al usuario."""
    while True:
        resp = input(f"{mensaje} (S/N): ").strip().upper()
        if resp in ["S", "Y"]:
            return True
        if resp in ["N"]:
            return False
        print("Opción inválida. Ingrese S para confirmar o N para cancelar.")


# ==========================================
# 2. VALIDACIONES DE REGLAS DE NEGOCIO Y DTO
# ==========================================

def validar_correo(correo: str) -> bool:
    """Valida sintaxis de correo electrónico."""
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, correo))

def validar_horas_trabajo(horas: float) -> bool:
    """Valida que la cantidad de horas asignadas a un RegistroTiempo sea razonable."""
    if 0.5 <= horas <= 24.0:
        return True
    print("Error: Las horas registradas deben estar entre 0.5 y 24.0 horas.")
    return False

def validar_formato_informe(formato: str) -> bool:
    """Valida que el formato del informe sea soportado."""
    formatos_valida = ["PDF", "CSV", "EXCEL", "TXT"]
    return formato.upper() in formatos_valida


# ==========================================
# 3. INTERFACES DE VALIDACIÓN Y FLUJO (MENÚS)
# ==========================================

# --- DEPARTAMENTO ---
def validate_crear_departamento():
    print("\n------------------------------")
    print(" Crear Departamento ")
    print("------------------------------")
    nombre = solicitar_texto("Nombre del Departamento: ", min_len=3)
    
    # AQUÍ LLAMAS A TU DTO / DAO:
    # Ej: DepartamentoDTO().crear_departamento(nombre)
    print(f"-> Validación exitosa para Departamento: '{nombre}'")

def validate_agregar_empleado_dept():
    print("\n------------------------------")
    print(" Agregar Empleado a Depto ")
    print("------------------------------")
    id_emp = solicitar_texto("ID Empleado: ")
    id_dept = solicitar_texto("ID Departamento: ")
    
    # Validar existencia con tu DTO antes de asignar
    print(f"-> Empleado '{id_emp}' asignado a Depto '{id_dept}'.")


# --- EMPLEADO Y USUARIO ---
def validate_crear_empleado():
    print("\n------------------------------")
    print(" Registrar Empleado ")
    print("------------------------------")
    id_emp = solicitar_texto("ID Empleado: ")
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

    # AQUÍ LLAMAS A TU DTO:
    # Se recomienda sanitizar o cifrar el salario usando ValidadorSeguridadDTO si corresponde.
    print(f"-> Empleado '{nombre}' listo para registrarse en el DAO.")

def validate_login():
    print("\n------------------------------")
    print(" Autenticación de Usuario ")
    print("------------------------------")
    username = solicitar_texto("Username: ")
    password = solicitar_texto("Contraseña: ")
    
    # AQUÍ LLAMAS A TU DTO:
    # res = UsuarioDTO().autenticar(username, password)
    print(f"-> Intento de login para '{username}' procesado.")


# --- PROYECTO ---
def validate_crear_proyecto():
    print("\n------------------------------")
    print(" Crear Proyecto ")
    print("------------------------------")
    id_proy = solicitar_texto("ID Proyecto: ")
    nombre = solicitar_texto("Nombre del Proyecto: ", min_len=3)
    descripcion = solicitar_texto("Descripción: ")
    fecha_inicio = solicitar_fecha("Fecha de Inicio (YYYY-MM-DD): ")

    # AQUÍ LLAMAS A TU DTO:
    # ProyectoDTO().crear_proyecto(...)
    print(f"-> Proyecto '{nombre}' validado.")


# --- REGISTRO DE TIEMPO ---
def validate_registrar_tiempo():
    print("\n------------------------------")
    print(" Registrar Horas Trabajadas ")
    print("------------------------------")
    id_emp = solicitar_texto("ID Empleado: ")
    id_proy = solicitar_texto("ID Proyecto: ")
    fecha = solicitar_fecha("Fecha de trabajo (YYYY-MM-DD): ")
    
    while True:
        horas = solicitar_flotante("Cantidad de horas trabajadas: ")
        if validar_horas_trabajo(horas):
            break

    descripcion = solicitar_texto("Descripción de tareas realizadas: ", min_len=5)

    # AQUÍ LLAMAS A TU DTO:
    # RegistroTiempoDTO().registrar_tiempo(...)
    print(f"-> Registro de {horas} hrs en proyecto '{id_proy}' validado correctamente.")


# --- INFORME (ADMINISTRADOR) ---
def validate_generar_informe():
    print("\n------------------------------")
    print(" Generar e Imprimir Informe ")
    print("------------------------------")
    criterios = solicitar_texto("Criterios de filtrado (Ej: Depto=IT): ")
    
    while True:
        formato = solicitar_texto("Formato de salida (PDF/CSV/EXCEL): ").upper()
        if validar_formato_informe(formato):
            break
        print("Error: Formato no soportado. Elija PDF, CSV o EXCEL.")

    # AQUÍ LLAMAS A TU DTO / DAO:
    # InformeDTO().generar_informe(...)
    print(f"-> Solicitud de informe en formato '{formato}' enviada.")


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
    """Valida la selección del menú."""
    while True:
        opc = solicitar_entero("Seleccione una opción: ")
        if 1 <= opc <= max_opc:
            return opc
        print(f"Opción no válida. Ingrese un valor entre 1 y {max_opc}.")

def inicial():
    """Bucle principal de la aplicación."""
    while True:
        menu_principal()
        opc = valida_opc(6)
        
        if opc == 1:
            print("\n1. Login | 2. Crear Empleado")
            sub_opc = valida_opc(2)
            if sub_opc == 1: validate_login()
            elif sub_opc == 2: validate_crear_empleado()

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
            validate_generar_informe()

        elif opc == 6:
            if solicitar_confirmacion("¿Está seguro que desea salir del sistema?"):
                print("Aplicación finalizada.")
                break

if __name__ == "__main__":
    inicial()