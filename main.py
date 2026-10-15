from vista.validaciones import menu_principal, validate_login


##### login
intentos = 1
print("Sistema POO")
while intentos <= 3:
    try:
        usuario = validate_login()
        if usuario is not None:
            print(f"Bienvenido(a) Sr(a). : {usuario.getUsername()}")
            menu_principal()
            break
        else:
            print("usuario o contraseña incorrecta")
            intentos += 1
    except:
        print("intentar nuevamente")
if intentos == 4:
    print("contraseña bloqueada")