Nota1 = float(input("Ingresa la nota 1: "))
Nota2 = float(input("Ingresa la nota 2: "))
Nota3 = float(input("Ingresa la nota 3: "))
Nota4 = float(input("Ingresa la nota 4: "))
Nota5 = float(input("Ingresa la nota 5: "))

promedio = (Nota1+Nota2+Nota3+Nota4+Nota5)/5
print("El promedio de las 5 notas es: ",round(promedio,1))

if promedio >= 60:
    print("Aprobado")
if 40 <= promedio <=59:
    print("En recuperación")
elif promedio <=39:
    print("Reprobado")




