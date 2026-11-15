from vista.validaciones import inicial, validate_login, banner

MAX_INTENTOS = 3


def main() -> None:
    banner("ECOTECH SOLUTIONS", "Gestión de tiempos y proyectos")

    intento = 0
    while intento < MAX_INTENTOS:
        try:
            usuario = validate_login()
        except KeyboardInterrupt:
            print("\n  [!] Interrupción detectada. El sistema no puede cerrarse con Ctrl+C.\n")
            continue
        except Exception:
            usuario = None

        if usuario is not None:
            print(f"\n  Bienvenido(a), {usuario.getNombreUsuario()}  [{usuario.getRol()}]")
            inicial(usuario)
            return

        intento += 1
        restantes = MAX_INTENTOS - intento
        if restantes > 0:
            print(f"  [!] Usuario o contraseña incorrectos. Intentos restantes: {restantes}\n")

    print("\n  [X] Acceso bloqueado: demasiados intentos fallidos.")


if __name__ == "__main__":
    main()