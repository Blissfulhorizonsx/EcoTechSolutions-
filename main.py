from vista.validaciones import inicial, validate_login, banner

MAX_INTENTOS = 3


def main() -> None:
    banner("ECOTECH SOLUTIONS", "Gestión de tiempos y proyectos")

    for intento in range(1, MAX_INTENTOS + 1):
        try:
            usuario = validate_login()
        except Exception as ex:
            print(f"  [!] Error del sistema: {ex}")
            usuario = None

        if usuario is not None:
            print(f"\n  Bienvenido(a), {usuario.getNombreUsuario()}  [{usuario.getRol()}]")
            inicial(usuario)
            return

        restantes = MAX_INTENTOS - intento
        if restantes > 0:
            print(f"  [!] Usuario o contraseña incorrectos. Intentos restantes: {restantes}\n")

    print("\n  [X] Acceso bloqueado: demasiados intentos fallidos.")


if __name__ == "__main__":
    main()