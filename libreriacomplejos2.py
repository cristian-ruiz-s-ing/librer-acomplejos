from sys import stdin
import math
import libreriacomplejos

def sumavector(m1,m2):
    """
    Esta función realiza...
    """
    return suma_de_matrices(m1,m2)

def resta_vector(m1,m2):
    return resta_matrices(m1,m2)

def escalar_vector(e,m1):
    return multiescalar(e,m1)

def transvector(m1):
    return transpuesta(m1)

def conjector(m1):
    return conjugada(m1)

def dagavec(m1):
    return daga(m1)
            

def suma_de_matrices(m1,m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        resp=[]
        for i in range(len(m1)):
            f=[]
            for j in range(len(m1[0])):
                x=libreriacomplejos.suma(m1[i][j],m2[i][j])
                f.append(x)

            resp.append(f)
        return resp
    else:
        return '¡No son compatibles!'

def resta_matrices(m1,m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        resp=[]
        for i in range(len(m1)):
            f=[]
            for j in range(len(m1[0])):
                x=libreriacomplejos.resta(m1[i][j],m2[i][j])
                f.append(x)

            resp.append(f)
        return resp
    else:
        return '¡No son compatibles!'

def multiescalar(e,m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j]=libreriacomplejos.mult(e,m1[i][j])
    return m1

def transpuesta(m1):
    resp=[]
    for j in range(len(m1[0])):
        f=[]
        for i in range(len(m1)):
            f.append(m1[i][j])
        resp.append(f)
    return resp

def conjugada(m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j]=libreriacomplejos.conj(m1[i][j])
    return m1

def daga(m1):
    return conjugada(transpuesta(m1))
    

def multimatriz(m1,m2):
    resp=[]
    if len(m1[0])==len(m2):
        for i in range(len(m1)):
            f=[]
            for j in range(len(m2[0])):
                x=(0,0)
                for k in range(len(m1[i])):
                    x=libreriacomplejos.suma(x,libreriacomplejos.mult(m1[i][k],m2[k][j]))
                f.append(x)
            resp.append(f)
        
        return resp
    else:
        return '¡No son compatibles!'

def prodinterno(v1,v2):
    resp=multimatriz(dagavec(v1),v2)
    '''for i in range(len(resp)):
        for j in range(len(resp[0])):
            x=libreriacomplejos.suma(x,resp[i][j])'''
    return resp[0][0]
            

def normatriz(m1):
    return math.sqrt(float(prodinterno(m1,m1)[0]))

def distancia(v1,v2):
    resp=resta_vector(v1,v2)
    '''x=(0,0)
    for i in range(len(resp)):
        for j in range(len(resp[0])):
            x=libreriacomplejos.suma(x,resp[i][j])'''
    return normatriz(resp)

def unitaria(m1):
    m2=daga(m1)
    resp=multimatriz(m1,m2)
    es_unitaria=True
    for i in range(len(resp)):
        for j in range(len(resp[0])):
            if i==j:
                if resp[i][j]== (1,0):
                    es_unitaria=es_unitaria and True
                else:
                    es_unitaria=False
                    return es_unitaria
            else:
                if resp[i][j]== (0,0):
                    es_unitaria=es_unitaria and True
                else:
                    es_unitaria=False
                    return es_unitaria
    return es_unitaria

def hermitiana(m1):
    if m1==daga(m1):
        return True
    else:
        return False

def tensor(m1,m2):
    filas=len(m1)*len(m2)
    columnas=len(m1[0])*len(m2[0])
    k=len(m2)
    l=len(m2[0])
    c=[]
    for m in range(filas):
        f=[]
        for n in range(columnas):
            f.append(0)
        c.append(f)

    for i in range(len(c)):
        for j in range(len(c[0])):
            a1=i//k
            a2=j//l
            b1=i%k
            b2=j%l
            c[i][j]=libreriacomplejos.mult(m1[a1][a2],m2[b1][b2])
    return c
    

def main():
    v1=[[(4,3)],[(5,8)]]
    v2=[[(7,15)],[(35,81)]]
    m1=[[(-6,2),(0,6),(7,2)],[(6,9),(7,7),(-6,-6)],[(5,8),(-6,8),(6,9)]]
    m2=[[(9,-6),(-3,-4),(5,-2)],[(3,6),(-1,-5),(0,-5)],[(9,9),(8,-4),(-8,-4)]]
    p=[[(3,0),(2,-1),(0,-3)],[(2,1),(0,0),(1,-1)],[(0,3),(1,1),(0,0)]]
    e=(5,0)

    #print(suma_de_matrices(m1,m2))
    #print(resta_matrices(v1,v2))
    #print(multiescalar(e,m1))
    #print(multimatriz(daga(v1),v1))
    #print(transpuesta(m1))
    #print(conjugada(v1))
    #print(daga(v1))
    #print(prodinterno(v1,v1))
    #print(normatriz(m1))
    #print(distancia(v1,v2))
    #print(unitaria(p))
    #print(hermitiana(p))
    print(tensor(m1,m2))
    
        
    
    
main()
