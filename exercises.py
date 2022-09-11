

#1  crear una lista de notas de 15 estudiantes , crear un vector donde se guarden los datos y calcular el promedio    [= ) $] 





class Estudiantes:

    def promedio():
        estNotas = []
        nombEstudiantes = []
        
        print('Este programa recoge los nombres y las notas de 15 estudiantes y devuelve el promedio     ')
        for i in range(15):

            nombre = input('   Ingrese el nombre de el estudiante    ')
            nota = float(input('Ingrese la nota del estudiante    ',))
            i = +1

            nombEstudiantes.append(nombre)
            estNotas.append(nota)
            prmedioNotas = (sum(estNotas) / 15)

            print('Resultados :  ', nombEstudiantes,  estNotas)
            print('Promedio: ',   prmedioNotas)







#2  Escriba un programa que dado un arreglo unidireccional que contiene numeros enteros.
#Determine cuantos de ellos son positivos , cuantos son negativos y cuantos son nulos [= ) $]



from itertools import count


class secondExample:
    def proG2():
        contenedor = [1 , 2  , 5 , -8 , -10 , 0 , -7 , 8 , 4 , 9]  #creamos los arrglos para guardarlos
        positivos = []                                            
        negativos = []
        nulo = []
        for i in contenedor:         #Mediante un ciclo for recorro el arreglo principal llamado contenedor
           if i/2 > 0:               #cada ves que (i) pasa por cada unos de los espacios del contenedor adquiere el valor
            positivos.append(i)      #con ese valor realizo un condicional if en el que le pregunto a i cuando me lo divida en 2 si su valor es mayor, menor o nulo
           elif i/2 <0:              #con esos condicionales lo que hago es guardarlos en los nuevos arreglos ya creados  y usando la funcion len contar cada unos de los numeros
            negativos.append(i)
           else:
            nulo.append(i)
            i =+1


        pos = len(positivos)
        neg = len(negativos)
        nlo = len(nulo)
               
            
        print('Los numeros de el arreglo unidireccional son   ' , contenedor)
        print('el arreglo tiene  : ' , "positivos  " ,  pos ,  "Negativos  "  ,neg ,  "Nulos  " , nlo)




#3 Suponga que en una eleccion hubo 5 candidatos, Los votos de los candidatos se digitan a como van llegando 
#Construya un programa que pueda proporcionar las siguientes informacion.  
# -Calcule el numero de votos de cada candidato y muestrelo por pantalla
# -Imprima por pantalla el candidato ganador y el numero de votos se asume que el ganador no empato


class eleccion:
    def votos():
        candidatos = [ 'carlos' , 'mauricio ' , 'eduardo ' , ['ferney' , 'ricardo']]
        candida2 =    { 'carlos ' , 'andrea ' , 'raul' }
        
        noVotos = []
        print (candidatos)
            