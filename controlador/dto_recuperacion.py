import os
import secrets
import bcrypt
from dao.dao_recuperacion import DaoRecuperacion
from controlador.dto_usuario import UsuarioDTO
from controlador.dto_empleado import EmpleadoDTO
from seguridad.servicio_correo import enviar_correo


class RecuperacionDTO:
    minutos_validez = 15
    segundos_entre_solicitudes = 60
    max_intentos_codigo = 5
    min_largo_clave = 8

    mensaje_generico = ("Si el usuario existe y tiene un correo registrado, "
                        "se envió un código de recuperación.")

    def solicitarCodigo(self, nombreUsuario: str) -> str:
        usuario = UsuarioDTO().buscarUsuario(nombreUsuario.strip())
        if usuario is None:
            return self._dbg("usuario no existe")

        emp = EmpleadoDTO().buscarPorUsuario(usuario.getIdUsuario())
        if emp is None:
            return self._dbg("El usuario no tiene empleado asociado")

        correo = emp.obtenerCorreoDescifrado()
        if "@" not in correo:
            return self._dbg(f"Correo inválido tras descifrar: {correo!r}")

        idUsuario = usuario.getIdUsuario()
        if DaoRecuperacion().solicitudesRecientes(idUsuario, self.segundos_entre_solicitudes) > 0:
            return self.mensaje_generico

        codigo = f"{secrets.randbelow(1_000_000):06d}"
        codigoHash = bcrypt.hashpw(codigo.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        if DaoRecuperacion().solicitudesRecientes(idUsuario, self.segundos_entre_solicitudes) > 0:
            return self._dbg("Solicitud demasiado reciente (60s)")

        if not DaoRecuperacion().crear(idUsuario, codigoHash, self.minutos_validez):
            return self._dbg("Fallo insertar en recuperacion_clave")

        cuerpo = (f"Hola {emp.getNombEmplea()},\n\n"
                  f"Tu código para restablecer la contraseña es: {codigo}\n"
                  f"Vence en {self.minutos_validez} minutos y solo sirve una vez.\n\n"
                  "Si no lo solicitaste, ignora este correo.")
        enviado = enviar_correo(correo, "Recuperación de contraseña - Ecotech", cuerpo)

        if not enviado and os.getenv("RECUPERACION_DEMO") == "1":
            print(f"  [DEMO] Código de recuperación: {codigo}")
        return self.mensaje_generico
    
    def _dbg(self, msg: str) -> str:
        if os.getenv("RECUPERACION_DEMO") == "1":
            print(f" [DEBUG] {msg}")
        return self.mensaje_generico

    def restablecer(self, nombreUsuario: str, codigo: str, nuevaClave: str) -> tuple:
        invalido = (False, "Código inválido o expirado.")

        if len(nuevaClave) < self.min_largo_clave:
            return (False, f"La contraseña debe tener al menos {self.min_largo_clave} caracteres.")

        usuario = UsuarioDTO().buscarUsuario(nombreUsuario.strip())
        if usuario is None:
            return invalido

        idUsuario = usuario.getIdUsuario()
        rec = DaoRecuperacion().buscarVigente(idUsuario)
        if rec is None:
            return invalido

        if rec["intentos"] >= self.max_intentos_codigo:
            DaoRecuperacion().marcarUsado(rec["idRecuperacion"])
            return (False, "Demasiados intentos. Solicite un código nuevo.")

        if not bcrypt.checkpw(codigo.strip().encode("utf-8"), rec["codigoHash"].encode("utf-8")):
            DaoRecuperacion().sumarIntento(rec["idRecuperacion"])
            return invalido

        mensaje = UsuarioDTO().cambiarPassword(idUsuario, nuevaClave)
        if "satisfactoriamente" not in mensaje:
            return (False, mensaje)

        DaoRecuperacion().marcarUsado(rec["idRecuperacion"])
        return (True, "Contraseña modificada satisfactoriamente. Ya puede iniciar sesión.")