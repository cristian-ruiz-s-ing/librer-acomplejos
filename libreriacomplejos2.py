from sys import stdin
import math
import libreriacomplejos

def sumavector(m1,m2):
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
    

def main():
    v1=[[(4,3)],[(5,8)]]
    v2=[[(7,15)],[(35,81)]]
    m1=[[(-6,2),(0,6),(7,2)],[(6,9),(7,7),(-6,-6)],[(5,8),(-6,8),(6,9)]]
    m2=[[(9,-6),(-3,-4),(5,-2)],[(3,6),(-1,-5),(0,-5)],[(9,9),(8,-4),(-8,-4)]]
    e=(5,0)

    #print(suma_de_matrices(m1,m2))
    #print(resta_matrices(v1,v2))
    #print(multiescalar(e,m1))
    #print(transpuesta(m1))
    #print(conjugada(v1))
    #print(daga(v1))
    #print(prodinterno(v1,v1))
    #print(normatriz(m1))
    print(distancia(v1,v2))
    #print(multimatriz(daga(v1),v1))
        
    
    
main() 
