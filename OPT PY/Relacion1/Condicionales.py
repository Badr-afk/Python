#1.Escribe un programa que recoja un número e indique si se trata de un número par o impar..
a=int(input("Dame un valor:"))

if a%2==0:
    print("El número es par")
else:
    print("El número es impar")  

#2. Escribe un programa que recoja un número por teclado y muestre el día de la
#semana que es (1 = Lunes, 2 = Martes...). En caso de introducir un número
#incorrecto, mostrará el mensaje “Día de la semana incorrecto”. 

numDia=int(input("Dame un número del dia de la semana:"))

match numDia:
    case 1:
        print("Es Lunes")
    case 2:
        print("Es Martes")    
    case 3:
        print("Es Miercoles")   
    case 4:
        print("Es Jueves")    
    case 5:
        print("Es Viernes")
    case 6:
        print("Es Sabado")    
    case 7:
        print("Es Domingo") 
    case _:
        print("Dia inexistente")       

#3. Escribe un programa que lea tres números y que muestre los números mayor
#y menor.        

a=int(input("Dame el primer número:"))
b=int(input("Dame el segundo número:"))
c=int(input("Dame el tercer número:"))

mayor=max(a,b,c)
menor=min(a,b,c)

print("El número más grande es: ",mayor)
print("El número más pequeño es: ",menor)

#4. Escribe un programa que recoja dividendo y divisor, y realice su división
#siempre que el divisor sea distinto de cero.

dividendo=float(input("Dame el dividendo:"))
divisor=float(input("Dame el divisor:"))

if dividendo==0:
    print("El dividendo no puede ser 0")
else:
    resultado=dividendo/divisor
    print("El resultado es: ",resultado)

#5. Escribe un programa que calcule el precio de entrada a un museo a partir de
#la edad del visitante, teniendo en cuenta que:
#a. Menores de 5 años entran gratis.
#b. Niños entre 5 años y 18 (sin llegar a los 18) pagan 3€.
#c. Mayores de edad hasta los 65 (sin llegar a los 65) pagan 6€.
#d. Jubilados entran gratis.

edad=int(input("Dime tu edad:"))    

if edad<5:
    print("Tu entrada es gratuita")
elif edad>=5 and edad<18: 
    print("Tu entrada cuesta 3€")
elif edad>=18 and edad<65:
    print("Tu entrada cuesta 6€")    
elif edad>=65:
    print("Tu entrada es gratuita")    


#6. Escribe un programa que muestre la nota final de un alumno a partir de su
#calificación numérica (valor decimal), teniendo en cuenta que:
#a. Nota menor de 5 es suspenso.
#b. Nota entre 5 y 6 (sin llegar) es suficiente.
#c. Nota entre 6 y 7 (sin llegar) es bien.
#d. Nota entre 7 y 9 (sin llegar) es notable.
#e. Nota entre 9 y 10 (sin llegar) es sobresaliente.
#f. Nota igual a 10 es matrícula de honor.
#g. Cualquier otro valor numérico fuera de este rango es un error.

nota=int(input("Dame tu nota:")) 

def calcularNota(nota):
    if nota<5:
        return("Suspenso")
    elif nota>=5  and nota<6:
         return("Suficiente")    
    elif nota>=6 and nota<7:
        return("Bien")    
    elif nota>=7 and nota<9:
        return("Notable")    
    elif nota>=9 and nota<10:
         return("sobresaliente")    
    elif nota==10:
        return("Matricula de honor") 

print(calcularNota(nota)) 


#7. Escribe un programa que recoja la hora del día y devuelva un saludo, según
#las siguientes reglas:

hora=int(input("Dime la hora:"))
def interpretarHora(hora):
    
    if hora>=7 and hora<12:
        return("Buenos Dias")
    elif hora>=12 and hora<20:
        return("Buenas tardes")
    elif hora>=20 and hora<23:
        return("Buenas noches")
    elif hora>=23:
        return("La hora no es correcta(0-23)")
    


print(interpretarHora(hora))


#8. Escribe un programa que recoja un mes del año (en número) y devuelva el
#número de días que tiene el mes. En caso de indicar un mes incorrecto deberá
#mostrar un mensaje de error.

comprobador=False;

while comprobador==False:
    
    mes=int(input("Dime el mes:"))
    
    match(mes):
        case 1:
            print("Enero tiene 31 dias")
            comprobador=True
        case 2:
            print("Febrero tiene 28 dias(29 si es bisiestos)")
            comprobador=True
        case 3:
            print("Marzo tiene 31 dias")
            comprobador=True    
        case 4:
            print("Abril tiene 30 dias")
            comprobador=True
        case 5:
            print("Mayo tiene 31 dias")
            comprobador=True
        case 6:
            print("Junio tiene 30 dias")
            comprobador=True       
        case 7:
            print("Julio tiene 31 dias")
            comprobador=True
        case 8:
            print("Agosto tiene 31 dias")
            comprobador=True
        case 9:
            print("Septiembre tiene 30 dias")
            comprobador=True
        case 10:
            print("Octubre tiene 31 dias")
            comprobador=True
        case 11:
            print("Noviembre tiene 30 dias")
            comprobador=True
        case 12:
            comprobador=True
            print("Diciembre tiene 31 dias") 
        case _:
            print("Mes inexistente (solo puede ser del 1 al 12)")
            comprobador=False
            
#9. Escribe un programa que recoja un año e indique si se trata de un año bisiesto
#o no. Un año es bisiesto si cumple estas condiciones:
#a. El año es divisible por 4.
#b. Si además el año es divisible por 100, debe ser también divisible por
#400.
#Ejemplos:
#- 1992 es bisiesto (cumple el caso a. Al no ser divisible por 100 no aplica el
#caso b)
#- 2023 no es bisiesto (no cumple ningún caso)
#- 2000 es bisiesto (cumple los casos a y b)
#- 1900 no es bisiesto (cumple el caso a, pero no el b porque es divisible por
#100 y no por 400)

año=int(input("Dame un año:"))

def esBisiesto(año):
    if año%4==0:
        if año%100==0:
            if año%400==0:
                return("El año es bisiesto")
            else:
                return("El año no es bisiesto")
        else:
            return("El año es bisiesto")    
    else:
        return("El año no es bisiesto")
    
print(esBisiesto(año))


#10.Escribe un programa que a partir de información de un donante determine si
#puede donar sangre. Las condiciones para donar son:
#a. No se debe donar en ayunas.
#b. Edad: Comprendida entre los 18 y 65 años.
#c. Peso: Superior a 50kg.
#d. Tensión arterial: dentro de límites adecuados para la extracción.
#i. Tensión diastólica (baja): entre 50mm Hg y 100 mm Hg
#ii. Tensión sistólica (alta): entre 90mm y 180mm Hg
#e. Pulso (frecuencia cardiaca): entre 50 y 110 pulsaciones
#f. Valores de hemoglobina:
#i. En hombres: superior a 13,5 gramos por litro
#ii. En mujeres: superior a 12,5 gramos por litro.
#g. Plaquetas: más de 150.000 cc
#h. Proteínas totales: más de 6 gr/dl.

ayuna=int(input("Esta en ayuna(1=si,0=no):"))

comprobador=True

if(ayuna==1):
    comprobador=True;
elif(ayuna==0):
    comprobador=False;

if comprobador==False:
    print("Lo siento,tenias que venir en ayunas,no puedes donar sangre")
else:
    edad10=int(input("Dime tu edad:"))

    if(edad<18 and edad>65):
        print("No tienes la edad requerida(18-65 años)")
    else:
        peso=float(input("Dime tu peso:"))

        if(peso<50):
            print("Tu peso es menor a la peso minimo(50)")  
        else:
            tensionDiastotica=int(input("Dime tu tension diastotica"))

            if(tensionDiastotica<50 and tensionDiastotica>100):
                print("La tensión diastotica no esta en el ranago requerido")

            else: 
                tensionSistotica=int(input("Dime tu tensión sistótica:"))

                if(tensionSistotica<90 and tensionSistotica>180):
                    print("La tension diastotica no esta en el rango requerido") 
                else:
                    pulso=int(input("Dime tu frecuencia cardiaca:"))  
                    if(pulso<50 and pulso>110):
                        print("Tu pulso no esta en rango permitido")
                    else:
                        genero=input()
