# t = input("Digite que quiere convertir: ")

# x = float (
#     input("Digite el valor que quiere convertir: ")
# )

# if t == "segundos" :
    
#     minutos1=(x/60)
#     horas2=(x/3600)
    
#     print(minutos1,"Minutos")
#     print(horas2, "Horas")
    
    
# else :
    
#     if t == "minutos" :
        
#         segundos1=(x*60)
#         horas1=(x/60)
        
#         print(segundos1,"Segundos")
#         print(horas1, "Horas")
        
#     else : 
        
#             if t == "horas":
#                 segundos3=(x*3600)
#                 minutos3=(x*60)
                
#                 print (segundos3, "Segundos")
#                 print (minutos3, "Minutos")
                
                
print("1 segundos")
print("2 minutos")
print("3 horas")
print("4 Salir")

op = input("seleeccione la opcion que desea convertir: ")
x = float (input("Digite el valor que quiere convertir: "))

if op == "1" :
    
    minutos1=(x/60)
    horas2=(x/3600)
    print(minutos1,"Minutos")
    print(horas2, "Horas")

elif op == "2" :
    
    segundos1=(x*60)
    horas1=(x/60)
    print(segundos1,"Segundos")
    print(horas1, "Horas")
    
elif op == "3" : 

    segundos3=(x*3600)
    minutos3=(x*60)
    print (segundos3, "Segundos")
    print (minutos3, "Minutos")
        

else:
    print ("Adios!!")
