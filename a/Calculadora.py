res=0

print("Bienvenido a la calculadora")

print(" ")
print("1 Sumar")
print("2 Restar")
print("3 Multiplicación")
print("4 División")
print("5 Salir")
print(" ")
a = input("Digite la operación a realizar: ")

if (a == "5"):
     print("¡ADIOS!")
else:
     x1 = float(input("Digite un número: "))
     x2 = float(input("Digite otro número: "))
     if (a == "1"):
          res=int(x1+x2)
          print("El resultado de la suma es: ",res)
     elif (a == "2"):
          res=int(x1-x2)
          print("El resultado de la resta es: ",res)
     elif (a == "3"):
          res=int(x1*x2)
          print("El resultado de la Multiplicación es: ",res)
     elif (a == "4"):
          if (x2==0):
               print("Error: no se puede dividir entre 0")
               print("Digite otro número")
          else:
               res=float(x1/x2)
               print("El resultado de la división es: ",res)

     

     
