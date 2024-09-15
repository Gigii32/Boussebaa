print("Hello world!")
name = input("Add meg a neved: ")
print(f"Szia, {name}!")
number = int(input("Adj meg egy számot: "))
print(f"A kétszerese: {number * 2}")
a = float(input("Add meg az első számot: "))
b = float(input("Add meg a második számot: "))

print(f"Összeg: {a + b}")
print(f"Különbség: {a - b}")
print(f"Szorzat: {a * b}")

if b != 0:
    print(f"Hányados: {a / b}")
else:
    print("A második szám nem lehet nulla, így nincs hányados.")
    a = int(input("Add meg az első számot: "))
b = int(input("Add meg a második számot: "))

if a > b:
    print(f"A nagyobb szám: {a}")
elif b > a:
    print(f"A nagyobb szám: {b}")
else:
    print("A két szám egyenlő.")
    a = int(input("Add meg az első számot: "))
b = int(input("Add meg a második számot: "))
c = int(input("Add meg a harmadik számot: "))

legkisebb = min(a, b, c)
print(f"A legkisebb szám: {legkisebb}")
a = float(input("Add meg az első oldal hosszát: "))
b = float(input("Add meg a második oldal hosszát: "))
c = float(input("Add meg a harmadik oldal hosszát: "))

if a + b > c and a + c > b and b + c > a:
    print("Ezekkel az oldalhosszal szerkeszthető háromszög.")
else:
    print("Ezekkel az oldalhosszal nem szerkeszthető háromszög.")