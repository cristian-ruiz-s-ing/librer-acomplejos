from sys import stdin
import libreriacomplejos

def suma_de_matrices(m1,m2):
    if d1 == d2:
        for i in range(int(d1[0])):
            f=[]
            for j in range(int(d1[1])):
                x=libreriacomplejos.suma(m1[i][j],m2[i][j])
                f.append(x)

            resp.append(f)
        return resp
    else:
        return '¡No son compatibles!'
    

def main():
    '''d1=tuple(stdin.readline().strip().split(','))
    m1=[]
    for i in range(int(d1[0])):
        f=[]
        for j in range(int(d1[1])):
            x=tuple(stdin.readline().strip().split(','))
            f.append(x)
            
        m1.append(f)

    d2=tuple(stdin.readline().strip().split(','))
    m2=[]
    for i in range(int(d2[0])):
        f=[]
        for j in range(int(d2[1])):
            x=tuple(stdin.readline().strip().split(','))
            f.append(x)
            
        m2.append(f)
    m1=(m1,d1)
    m2=(m2,d2)'''
    m1=[[(5,2),(4,3)],[(7,1),(2,4)]]
    m2=[[(8,1),(9,20)],[(3,16),(4,5)]]

    print(suma_de_matrices(m1,m2))
        
    
    
main()       
