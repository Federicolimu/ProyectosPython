"""Activación de alarma.
Pregunta si hay movimiento y si el sistema está armado. Si ambas condiciones se cumplen, activa alarma. Si no, permanece en reposo."""

motion = input("¿Hay movimiento? Responde, si ó no ")
system = input("¿El sistema está armado? Responde, si ó no ")

if (motion == "si" and system == "si"):
    print("***ALARMA ACTIVADA***")
else:
    print("Sistema en reposo")