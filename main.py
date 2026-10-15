# CAMBIO: Se importa'inicial' en lugar de 'menu_principal'
from vista.validaciones import inicial, validate_login

##### login
intentos = 1
print("Sistema POO")
while intentos <= 3:
    try:
        usuario = validate_login()
        if usuario is not None:
            print(f"Bienvenido(a) Sr(a). : {usuario.getNombreUsuario()}")
            
            # CAMBIO 2: Llamar a inicial(usuario) para arrancar el bucle del sistema
            inicial(usuario)
            break
        else:
            print("usuario o contraseña incorrecta")
            intentos += 1
    except:
        print("intentar nuevamente")
if intentos == 4:
    print("contraseña bloqueada")