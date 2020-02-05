from sys import stdin
import math

def suma(c1,c2):
    resp=[0,0]
    resp[0]=float(c1[0])+float(c2[0])
    resp[1]=float(c1[1])+float(c2[1])
    t=(round(resp[0],3),round(resp[1],3))
    r=''
    if t[0]==0:
        if t[1]==0:
            r+=str(t[0])
        else:
            r+=str(t[1])+'i'
    else:
        if t[1]==0:
            r+=str(t[0])
        else:
            if t[1]>0:
                r+=str(t[0])+'+'+str(t[1])+'i'
            else:
                r+=str(t[0])+str(t[1])+'i'
    return t

def resta(c1,c2):
    resp=[0,0]
    resp[0]=float(c1[0])-float(c2[0])
    resp[1]=float(c1[1])-float(c2[1])
    t=(round(resp[0],3),round(resp[1],3))
    r=''
    if t[0]==0:
        if t[1]==0:
            r+=str(t[0])
        else:
            r+=str(t[1])+'i'
    else:
        if t[1]==0:
            r+=str(t[0])
        else:
            if t[1]>0:
                r+=str(t[0])+'+'+str(t[1])+'i'
            else:
                r+=str(t[0])+str(t[1])+'i'
    return t

def mult(c1,c2):
    resp=[0,0]
    resp[0]=float(c1[0])*float(c2[0])+((float(c1[1])*float(c2[1]))*-1)
    resp[1]=float(c1[0])*float(c2[1])+float(c1[1])*float(c2[0])
    t=(round(resp[0],3),round(resp[1],3))
    r=''
    if t[0]==0:
        if t[1]==0:
            r+=str(t[0])
        else:
            r+=str(t[1])+'i'
    else:
        if t[1]==0:
            r+=str(t[0])
        else:
            if t[1]>0:
                r+=str(t[0])+'+'+str(t[1])+'i'
            else:
                r+=str(t[0])+str(t[1])+'i'
    return t

def bonito(c2):
    x=''
    if float(c2[0])==0:
        if float(c2[1])==0:
            x+='0'
        else:
            if float(c2[1])==1:
                x+='i'
            else:
                x+=str(c2[1])+'i'
    else:
        if float(c2[1])==0:
            x+=str(round(c2[0],3))
        elif float(c2[1])>0:
            x+=str(round(c2[0],3))+'+'+str(round(c2[1],3))+'i'
        else:
            x+=str(round(c2[0],3))+str(round(c2[1],3))+'i'
    return x

def div(c1,c2):
    c3=[0,0]
    c3[0]=float(c2[0])
    c3[1]=float(c2[1])*-1
    x=mult(c1,c3)
    y=mult(c2,c3)
    return x+'/'+y

def modulo(c1):
    x=bonito(c1)
    a=((float(c1[0])**2)+(float(c1[1])**2))**(1/2)
    y=round(a,3)
    return y
    


def conj(c1):
    x=float(c1[0])
    y=float(c1[1])*-1
    resp=(x,y)
    x=bonito(resp)
    return resp

def polar(c1):
    r=((float(c1[0])**2)+(float(c1[1])**2))**(1/2)
    a=math.atan(float(c1[1])/float(c1[0]))
    r=round(r,3)
    a=round(a,3)
    coord=(r,a)
    return coord

'''def main():
    opc=int(stdin.readline().strip())
    if opc==1:
        c1=tuple(stdin.readline().strip().split(','))
        c2=tuple(stdin.readline().strip().split(','))
        print(suma(c1,c2))'''
