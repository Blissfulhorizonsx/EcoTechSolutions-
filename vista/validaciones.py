import getpass


def menuLogin():
    nombUsuario = input("Ingrese su nombre: ")
    print("Roles: (1) Administrador || (2) Empleado ") # Mandar aviso en caso de elegir mal un rol.
    rolUsuario = input("Ingrese su rol: ")  
    contraseña = getpass.getpass(prompt="Ingrese su contraseña correspondiente: ") # hacer que la contraseña se muestre como astericos(getpass)



def menuPrincipal():
    print("-" * 22)
    print()



menuLogin()