# la calculadora del papu :v

print ("1 suma")
print ("2 resta")
print ("3 multiplicacion")
print ("4 división")
print ("5 potencia")
print ("6 salir")

h = float
g = input("Ingrese la operación a realizar: ")

if g == "1" :
     print ("Ingrese los valores")
     op1 = float (input())
     op2 = float (input())
     res = int (op1+op2)

     print ("Resultado de la suma es: ",res)
elif g == "2" :

     print ("Ingrese los valores")
     op1 = float (input())
     op2 = float (input())
     res = int (op1-op2)
     print ("Resultado de la resta es: ",res)

elif g == "3" :
     print ("Ingrese los valores")
     op1 = float (input())
     op2 = float (input())

     res = int (op1*op2)
     print ("Resultado de la multiplicación es: ",res)

elif g == "4" :
     print ("Ingrese los valores")
     op1 = float (input())
     op2 = float (input())
     
     if op2 != 0 :

          res = float (op1/op2)
          print ("Resultado de la división: ",res)

     else :
               print ("Digite un divisor diferente de 0")
               
elif g == "5" :
     
     print ("Ingrese los valores")
     op1 = float (input())
     op2 = float (input())
     
     print ("El resultado de la potencia es: ", pow(op1, op2))

else :
     print("Adios")









