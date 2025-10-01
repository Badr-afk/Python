#Conceptos básicos
#1. Escriba un programa que recoja un valor por teclado y muestre de qué tipo es.
c=float(input("Dame un valor:"));
print("Es el del tipo de: " + str(type (c)));
#2 Escribe un programa que recoja dos números enteros por teclado y muestre los siguientes resultados: suma, resta, multiplicación, división real, divisiónentera, resto de la división entera y potencia.
num1=float(input("Dame el primer valor:"))
num2=float(input("Dame el segundo valor:"))

suma=num1+num2;
resta=num1-num2;
multiplicacion=num1*num2;
division=num1/num2;
divisionEnt=num1//num2
resto=num1%num2;
potencia=num1**num2;

print("La suma es: " , suma)
print("La resta es: " , resta)
print("La multiplicacion es: " , multiplicacion)
print("La division es: " , division)
print("La division entera es: " , divisionEnt)
print("El resto es: " , resto)
print("La potencia es: " , potencia)

#3. Escribe un programa que pida el nombre del usuario y le responda con un
#saludo. En el saludo deberá utilizarse el nombre que introdujo el usuario.

nombre = input("Dime tu nombre:")

print("Hola " + nombre)

#4. Escribe un programa que recoja tres números y calcule su media aritmética.

n1=float(input("Dame el prinmer valor:" ))
n2=float(input("Dame el segundo valor:" ))
n3=float(input("Dame el tercer valor:"))
media=(n1+n2+n3)/3

print("La media es: ",media);

#5 Escribe un programa que recoja un número y muestre su valor absoluto.

a=float(input("Dame un valor:"))

a_Absolute=abs(a)

print("El valor absoluto: ", a_Absolute)

#6.Escribe un programa que recoja las notas de las tres evaluaciones de un
#alumno. A continuación debe calcular y mostrar la nota final, teniendo en
#cuenta que la primera evaluación cuenta un 20% de la nota final, la segunda
#evaluación un 35% y la tercera evaluación un 45%.

nota1=float(input("Dame la nota de la primera evaluación:"))
nota2=float(input("Dame la nota de la segunda evaluación:"))
nota3=float(input("Dame la nota de la tercera evaluación:"))

notaFinal=((nota1*0.2)+(nota2*0.35)+(nota3*0.45))

print("La nota final se queda en: ", notaFinal)

#7.Escribe un programa que recoja un número y muestre su representación en
#código binario.
numeroReal=int(input("Dame un numero:"))

numeroBin=bin(numeroReal)

print("El resultado es: ",numeroBin)
#8.Escribe un programa que recoja un texto y lo muestre cinco veces
#consecutivas en la misma línea.

texto=input("Dame un texto:")

for i in range(5):
    print(texto) 

#9. Escribe un programa que recoja un texto y que muestre su longitud.
texto2=input("Dame una frase:")

total=len(texto2)

print("La frase tiene " , total , " letras")

#10.Escribe un programa que recoja la edad del usuario y muestre la edad que
#tendrá dentro de 5, 10 y 15 años.
edad=int(input("Dame tu edad:"))

enCinco=edad+5
enDiez=edad+10
enQuince=edad+15

print("Tu edad en 5 años sera de ",enCinco, " años")
print("Tu edad en 10 años sera de ", enDiez, " años")
print("Tu edad en 15 años sera de ", enQuince, " años")

