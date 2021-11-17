
def funcion(arg1,arg2): #se crea la funcion con dos variables de entrada, arg1= argumento1, arg2=argumento2
    try:
        listado=[]  
        for x in arg1:                              #accedemos a cada objeto dentro del primer argumento  
            for y in x:                             #leemos la llave de cada objeto                   
                if y in arg2 and x[y]==arg2[y]:     #comprpbar si las llaves y valores del argumento1 son iguales al del argumento2
                    listado.append(x)               #agrega en un nuevo arreglo los objetos que coincidieron
        resultado= print(listado)                   #entrega el resultado impreso ya al usuario
        return resultado         
    except TypeError:                                  #si se presenta un error con los arreglos
        print("los valores agregados no son arreglos, compruebe de nuevo porfavor.")


            
