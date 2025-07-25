"""Gasto semanal.
Solicita ingreso y gasto. Si el gasto es menor al 70% del ingreso, muestra “Gasto controlado”. Si no, “Gasto alto”."""

income = int(input("¿Cuántos son tus ingresos semanales? "))
expenses = int(input("¿Cuántos son tus gastos semanales? "))
income_less_70 = (income * 70) / 100
if (expenses < income_less_70):
    print("Gasto controlado")
else:
    print("Gasto alto")