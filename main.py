from calculator import Calculator


a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))

vypocet = Calculator()
print(f"Součet {a} a {b} je", vypocet.scitani(a, b))

print(f"Rozdíl {a} a {b} je", vypocet.odcitani(a, b))

print(f"Součin {a} a {b} je", vypocet.nasobeni(a, b))

print(f"Podíl {a} a {b} je", vypocet.deleni(a, b))
