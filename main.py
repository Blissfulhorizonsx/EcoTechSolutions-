from vista.validaciones import (
    inicial,
    validate_login,
    banner,
    mostrar_menu,
    valida_opc,
    validate_recuperar_clave,
)

MAX_INTENTOS = 3


def iniciar_sesion() -> None:
    intento = 0
    while intento < MAX_INTENTOS:
        try:
            usuario = validate_login()
        except KeyboardInterrupt:
            print("\n  [!] Interrupción detectada. El sistema no puede cerrarse con Ctrl+C.\n")
            continue
        except Exception:
            print("\n  [!] No fue posible validar las credenciales en este momento.\n")
            usuario = None

        if usuario is not None:
            print(f"\n  Bienvenido(a), {usuario.getNombreUsuario()}  [{usuario.getRol()}]")
            inicial(usuario)
            return

        intento += 1
        restantes = MAX_INTENTOS - intento
        if restantes > 0:
            print(f"  [!] Usuario o contraseña incorrectos. Intentos restantes: {restantes}\n")

    print("\n  [X] Acceso bloqueado: demasiados intentos fallidos.\n")


def main() -> None:
    banner("ECOTECH SOLUTIONS", "Gestión de tiempos y proyectos")

    while True:
        try:
            mostrar_menu("BIENVENIDO", ["Iniciar sesión", "Olvidé mi contraseña", "Salir"])
            opc = valida_opc(3)

            if opc == 1:
                iniciar_sesion()
            elif opc == 2:
                validate_recuperar_clave()
            elif opc == 3:
                print("\n  Saliendo del sistema. ¡Hasta pronto!")
                break

        except KeyboardInterrupt:
            print("\n  [!] Interrupción detectada. El sistema no puede cerrarse con Ctrl+C.\n")
        except Exception:
            print("\n  [!] Ocurrió un error inesperado en el sistema.\n")


if __name__ == "__main__":
    main()