import random
import math
import matplotlib.pyplot as plt

#Generación de genotipos
def genotipo(min, max):
    genotipos=[],
    individuo=[random.randint(min, max) for i in range(long_material_gen)]
    val = ''.join(str(e) for e in individuo)

    convertido=int((val), 2)

    if convertido >= 1 and convertido<=59:
        genotipos=individuo
        # print("Convertido "+str(convertido))
    else:
        genotipos=genotipo(0,1)
    return genotipos

#Generación de genotipo A
def poblacionA():
    return [genotipo(0,1) for i in range(num_indiviuo)]

#Generación de genotipo B
def poblacionB():
    return [genotipo(0,1) for i in range(num_indiviuo)]

#Cruza entre genotipos del mismo valor (A-A)
def cruza(poblacion):
    hijos=[]
    for x in range(0,len(poblacion),2):
        corte=random.randint(1, long_material_gen)
        # print("Punto cruza para pareja"+str(x)+" : "+ str(corte))
        hijos.append(poblacion[x][:corte]+poblacion[x+1][corte:])
        hijos.append(poblacion[x][corte:]+poblacion[x+1][:corte])
    print("Hijos: "+ str(hijos))
    return hijos

#Mutación de un genotipo en base a prob_mut
def mutacion(genoma):
    muta=""
    for i in range(long_material_gen):
        j = random.randint(1, 100)
        if j < prob_mut:   
            if genoma[i] == '1':
                muta=muta+'0'
            else:
                muta=muta+'1'
        else:
            muta=muta+genoma[i]
    genoma=muta    
    if int(genoma,2) <= 0 or int(genoma,2) > 59:
        muta=""
        for k in range(long_material_gen):
            l = random.randint(1, 100)
            if l < prob_mut:
                if genoma[k] == '1':
                    muta=muta+'0'
                else:
                    muta=muta+'1'
            else:
                muta=muta+genoma[k]
        genoma=muta
        return genoma
    else:
        return genoma

#Selección de los genotipos hijos tanto de A como B
def seleccion(hijos_de_A, hijos_de_B):
    EvaluadosI=[]
    EvaluadosF=[]
    var=0
    var2=num_indiviuo
    for i in range (0, len(valores_y)):
        for j in range(0,len(hijos_de_A)):
            #print("Arrai[i]: ",valores_i[i])
            #print("Arrai[x]: ",valores_x[i])
            val = ''.join(str(e) for e in hijos_de_A[j])
            individuo_A=int((val), 2)
            individuo_A=individuo_A*.10
            val2 = ''.join(str(e) for e in hijos_de_B[j])
            individuo_B = int((val2), 2)
            individuo_B = individuo_B*.10
            Resultado = valores_y[i]-math.cos(individuo_A*valores_x[i])*math.sin(individuo_B*valores_x[y])
            EvaluadosI.append([Resultado])
        EvaluadosF.append(EvaluadosI[var:var2])
        var=var2
        var2=var2+num_indiviuo
    posicion=union(EvaluadosF,hijos_de_A,hijos_de_B)
    return posicion

#Método extra para la separación del arreglo de seleccion. Ejemplo.[[1,0,0,1],[0001]]
def union(EvaluadosF,hijos_de_A,hijos_de_B):
    var = 0
    var2 = len(valores_y)
    arregloI=[]
    arregloF=[]
    promedio=[]
    posiciones=[]

    val = ''.join(str(e) for e in hijos_de_A[0])
    individuo_A=int((val), 2)
    individuo_A=individuo_A*.10
    val2 = ''.join(str(e) for e in hijos_de_B[0])
    individuo_B=int((val2), 2)
    individuo_B=individuo_B*.10
    print("TAMAÑO",len(EvaluadosF))
    # print("A ",individuo_A)
    # print("B ",individuo_B)
    for i in range(0,num_indiviuo):
        for j in range(0,len(EvaluadosF)):
            arregloI.append(EvaluadosF[j][i])
        arregloF.append(arregloI[var:var2])
        var = var2
        var2=var2+len(valores_y)

    print("PUNTOS ",arregloF[0])
    valores_y_2.clear()
    valores_y_2.append(arregloF[0])
    sumaPromedio=0
    for k in range(0,num_indiviuo):
        for l in range(0,num_indiviuo):
            val3 = ''.join(str(e) for e in arregloF[k][l])
            sumaPromedio=sumaPromedio+float(val3)
        sumaPromedio=sumaPromedio/num_indiviuo
        promedio.append(sumaPromedio)
        # print("Promedio: ",sumaPromedio)
    promedio_gen.append(sumaPromedio)
    # promedios_gen= sorted(promedio_gen)
    desordenado= promedio
    ordenado = sorted(promedio)
    print("O: ",ordenado)
    print("D: ",desordenado)
    mejor_caso.append(ordenado[0])
    mejor_caso.sort(reverse=True)
    peor_caso.append(ordenado[-1])
    # mejores_caso = sorted(mejor_caso)
    # peores_caso = sorted(peor_caso)
    for j in range(0,len(ordenado)):
        for i in range(0,len(desordenado)):
            if ordenado[j]==desordenado[i]:
                numo = i
                posiciones.append(numo)
                break
    print("MEJOR A;B : ",hijos_de_A[posiciones[0]]," : ",hijos_de_B[posiciones[0]])        
    print("posiciones ",posiciones)
    print("Mejor caso: ",mejor_caso)
    print("Peor caso: ",peor_caso)
    print("Promedios: ",promedio_gen)
    return posiciones

def mejVal(x):
    bits_gener.clear()
    for y in range(6):
        bits_gener.append(int(pob_A[x][y]))
    return list(bits_gener)

#Metodo para graficar
def mostrarGrafica():
    plt.plot(valores_x, valores_y, label = "Real", color="green")
    plt.plot(valores_x, valores_y_2[0], label = "Apróx.", color="red")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráfica comparativa del Modelo original con el Modelo apróximado')
    plt.legend()
    plt.show()

#Metodo para graficar
def mostrarGrafica2():
    plt.plot(peor_caso,label = "Peor caso", color="green")
    plt.plot(promedio_gen, label = "Promedido", color="blue")
    plt.plot(mejor_caso, label = "Mejor caso", color="red")
    plt.xlabel('Generaciones')
    plt.ylabel('Fitness')
    plt.title('Fitness por generación')
    plt.legend()
    plt.show()

if __name__ == '__main__':

    valores_y=[0.0678,0.7622,0.1102,0.4269,1.0171,0.0950,-0.1299,0.3877,-0.4545,-0.7964,0.0448,-0.2894,-0.5247,0.5567,0.5318,0.0428,0.8382,0.7316,-0.2220,0.1784,0.1684]
    valores_x=[0.0000,0.2500,0.5000,0.75000,1,1.25,1.50,1.75,2,2.25,2.50,2.75,3,3.25,3.50,3.75,4,4.25,4.50,4.75,5]

    long_material_gen = 6 
    num_indiviuo = 20
    porcentaje_cruza=10
    numero_generaciones=10
    prob_mut=50
    bits_gener=[]
    valores_y_2=[]
    generacion= []
    promedio_gen=[]
    mejor_caso=[]
    peor_caso=[]

    pob_A = poblacionA()
    pob_B = poblacionB()

    for i in range(0,numero_generaciones):
        print("generación: ",i)
        generacion.append(i)
        cruza_A=cruza(pob_A)
        cruza_B=cruza(pob_B)
        pob_A.clear()

        for j in range(0,len(cruza_A)):
            val = ''.join(str(e) for e in cruza_A[j])
            convertido=str(val)
            pob_A.append(mutacion(convertido))
        
        for k in range(0,len(cruza_B)):
            val2 = ''.join(str(e) for e in cruza_B[k])
            convertido2 = str(val2)
            pob_B.append(mutacion(convertido2))

        for x in range(num_indiviuo):
            pob_A[x] = mejVal(x)
        # print(pob_A)

        for y in range(num_indiviuo):
            pob_B[y] = mejVal(y)
        # print(pob_B)
        
        posiciones=seleccion(pob_A,pob_B)
        pob_A_Nueva = []
        pob_B_Nueva = []

        for z in range(0,len(posiciones)):
            pob_A_Nueva.append(pob_A[posiciones[z]])
            pob_B_Nueva.append(pob_B[posiciones[z]])

        pob_A.clear()
        pob_B.clear()
        pob_A = pob_A_Nueva
        pob_B = pob_B_Nueva

    mostrarGrafica()
    mostrarGrafica2()




