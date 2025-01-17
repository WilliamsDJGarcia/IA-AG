import random
import math
import matplotlib.pyplot as plt

#Generación de genotipos
def genotipo():
    valor2 = []
    for i in range(poblacion_inicial):
        valor = random.randint(1,59)
        valor2.append(valor)
    return valor2

#Cruza entre genotipos del mismo valor (A-A) (B-B)
def cruza(genotipo):
    hijosA=[]
    hijosB=[]
    aux=[]
    aux2=[]
    A = genotipo[0]
    B = genotipo[1]
    
    for i,j in zip(A,B):
        val = converBin(i)
        val2 = converBin(j)
        aux.append(val)
        aux2.append(val2)

    for i in range(0,len(aux),2):
        corte=random.randint(1, long_material_gen)
        # print("Punto cruza para pareja "+str(i)+" : "+ str(corte))
        hijosA.append(aux[i][:corte]+aux[i+1][corte:])
        hijosA.append(aux[i][corte:]+aux[i+1][:corte])
    # print("HijosA: "+ str(hijosA))

    for i in range(0,len(aux2),2):
        corte=random.randint(1, long_material_gen)
        # print("Punto cruza para pareja "+str(i)+" : "+ str(corte))
        hijosB.append(aux2[i][:corte]+aux2[i+1][corte:])
        hijosB.append(aux2[i][corte:]+aux2[i+1][:corte])
    # print("hijosB: "+ str(hijosB))
    
    C = [hijosA]+[aux]+[hijosB]+[aux2]
    return C

#Mutación de un genotipo en base a prob_mut
def mutacion(genoma):
    originalA = genoma[1]
    originalB = genoma[3]
    genomaA = genoma[0]
    genomaB = genoma[2]
    A = []
    B = []

    for i in range(len(genomaA)):
        for j in range(len(genomaA[i])):
           rd = random.randint(1,100)
           val_bin = genomaA[i][j]

           if rd < prob_mut:
           
               if genomaA[i][j] == 1:
                   genomaA[i][j] = 0
               else:
                   genomaA[i][j] = 1
           else:
                genomaA[i][j]

    for i in range(len(genomaB)):
        for j in range(len(genomaB[i])):
           rd = random.randint(1,100)
           val_bin = genomaB[i][j]
       
           if rd < prob_mut:
               if genomaB[i][j] == 1:
                   genomaB[i][j] = 0
               else:
                   genomaB[i][j] = 1
           else:
                genomaB[i][j]

    A = genomaA
    B = genomaB
    C = [A]+[originalA]+[B]+[originalB]

    return C

#Método selección
def selecciona(A,B):
    generacion=[]
    mejores = []
    auxA = []
    auxB = []
    promedio = []
    aux = 0
    
    for i,j in zip(A,B):
        valory = []
        fit = 0
        pro=0
        individuo_A=i*.10
        individuo_B=j*.10

        for x in range(len(valores_x)):
            resultY = cosSin(valores_x[x],individuo_A,individuo_B)
            fit += (math.pow((valores_y[x]-resultY),2))
            valory.append(round(resultY,4))
            promedio.append(fit)
        fit = fit/len(valores_x)
        generacion.append([fit,i,j,valory])
    generacion.sort()
    
    for x in promedio:
        pro = pro+x
    pmd.append(pro/len(promedio))
    
    for z in generacion:
        aux = aux+z[0]
        ultimoValor = z[0]
        if len(mejores)<10:
            mejores.append(z)
    peor_caso_gen.append(ultimoValor)
    promedio_gen.append(aux/21)

    for l in mejores:
        auxA.append(l[1])
        auxB.append(l[2])
    
    auxC = [auxA]+[auxB]
    mejor_caso_gen.append(mejores[0])
    
    mejor.append(mejores[0][0])
    return auxC

#Convertidor
def converBin(num):
    binario="{0:06b}".format(num)
    return [int(i) for i in str(binario)]    

#Función para Y
def cosSin(i,individuo_A,individuo_B):
    valorY = math.cos(individuo_A*i)*math.sin(individuo_B*i)
    return valorY

# #Metodo para graficar
def mostrarGrafica():
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

    ax1.plot(valores_x, valores_y,label = "Real", color="green")
    ax1.plot(valores_x, valores_y_2, label = "Apróx.", color="red")
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_title('Gráfica comparativa del Modelo original con el Modelo apróximado')
    ax1.legend()

    ax2.plot(peor_caso_gen,label = "Peor caso", color="green")
    ax2.plot(promedio_gen, label = "Promedio", color="blue")
    ax2.plot(mejor, label = "Mejor caso", color="red")
    ax2.set_xlabel('Generaciones')
    ax2.set_ylabel('Fitness')
    ax2.set_title('Fitness por generación')
    ax2.legend()

    plt.show()

if __name__ == '__main__':

    valores_y=[0.0678,0.7622,0.1102,0.4269,1.0171,0.0950,-0.1299,0.3877,-0.4545,-0.7964,0.0448,-0.2894,-0.5247,0.5567,0.5318,0.0428,0.8382,0.7316,-0.2220,0.1784,0.1684]
    valores_x=[0.0000,0.2500,0.5000,0.75000,1,1.25,1.50,1.75,2,2.25,2.50,2.75,3,3.25,3.50,3.75,4,4.25,4.50,4.75,5]

    long_material_gen = 6
    poblacion_inicial = 20
    numero_generaciones=300
    prob_mut=50 #porcentaje

    valores_y_2=[]
    generacion= []
    promedio_gen=[]
    mejor_caso_gen = []
    mejor=[]
    peor_caso_gen=[]
    pmd = []

    pob_A = genotipo()
    pob_B = genotipo()

    for i in range(numero_generaciones):
        generacion.append(i)
        print("GENERACION ",i)
        seleccion = selecciona(pob_A,pob_B)
        cruz = cruza(seleccion)
        muta = mutacion(cruz)

        new_A = muta[0]+muta[1]
        new_B = muta[2]+muta[3]

        A =[]
        B = []
        for j,k in zip(new_A,new_B):
            val = ''.join(str(e) for e in j)
            individuo_A=int((val), 2)
            A.append(individuo_A)
            val2 = ''.join(str(e) for e in k)
            individuo_B=int((val2), 2)
            B.append(individuo_B)
            new_A = A
            new_B = B

        pob_A.clear()
        pob_B.clear()

        pob_A = new_A
        pob_B = new_B

    pmd.sort()
    mejor_caso_gen.sort()
    mejorFit = mejor_caso_gen[0]
    mejorA = mejor_caso_gen[0][1]
    mejorB = mejor_caso_gen[0][2]
    valores_y_2 = mejor_caso_gen[0][3]
    
    print("Y ",valores_y_2)
    print("A ",mejorA*.10)
    print("B ",mejorB*.10)
    print("BEST FIT ",pmd[0])

    mostrarGrafica()
