"""Reparto de dulces.
Pide cuántos dulces hay y cuántos niños. Si los dulces se reparten exactos, muestra “Reparto justo”. Si no, muestra cuántos sobran."""

candys = int(input("Cuantame. ¿Cuántos dulces tienes? "))
boys = int(input("Ahora dime, ¿Cuántos niños hay? "))
distribution = candys - boys 
amount = candys / boys
print(f"A cada niño le tocan {amount} dulces")

if (candys % boys == 0):
    print("Reparto justo")
else:
    print(f"Sobran {distribution} dulces")
