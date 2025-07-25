""". Verificación de ingreso.
Pregunta si el usuario está registrado y no está bloqueado. Si ambas condiciones se cumplen, acceso permitido. Si no, acceso denegado."""

register = input("¿Ya estás registrado en la plataforma? ")
block = input("¿Estás bloqueado en la plataforma? ")

if (register == "si" and block == "no"):

    print("Acceso permitido.")
else:
    print("Acceso denegado.")