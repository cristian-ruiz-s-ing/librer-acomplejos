from sys import stdin
import math

def suma(c1,c2):
    resp=[0,0]
    resp[0]=int(c1[0])+int(c2[0])
    resp[1]=int(c1[1])+int(c2[1])
    t=(resp[0],resp[1])
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
    return r

def resta(c1,c2):
    resp=[0,0]
    resp[0]=int(c1[0])-int(c2[0])
    resp[1]=int(c1[1])-int(c2[1])
    t=(resp[0],resp[1])
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
    return r

def mult(c1,c2):
    resp=[0,0]
    resp[0]=int(c1[0])*int(c2[0])+((int(c1[1])*int(c2[1]))*-1)
    resp[1]=int(c1[0])*int(c2[1])+int(c1[1])*int(c2[0])
    t=(resp[0],resp[1])
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
    return r

def bonito(c2):
    x=''
    if int(c2[0])==0:
        if int(c2[1])==0:
            x+='0'
        else:
            if int(c2[1])==1:
                x+='i'
            else:
                x+=str(c2[1])+'i'
    else:
        if int(c2[1])==0:
            x+=str(c2[0])
        elif int(c2[1])>0:
            x+=str(c2[0])+'+'+str(c2[1])+'i'
        else:
            x+=str(c2[0])+str(c2[1])+'i'
    return x

def div(c1,c2):
    c3=[0,0]
    c3[0]=int(c2[0])
    c3[1]=int(c2[1])*-1
    x=mult(c1,c3)
    y=mult(c2,c3)
    return x+'/'+y

def modulo(c1):
    x=bonito(c1)
    a=((int(c1[0])**2)+(int(c1[1])**2))**(1/2)
    y=round(a,3)
    return y
    


def conj(c1):
    resp=[0,0]
    resp[0]=int(c1[0])
    resp[1]=int(c1[1])*-1
    x=bonito(resp)
    return x

def polar(c1):
    r=((float(c1[0])**2)+(float(c1[1])**2))**(1/2)
    a=math.atan(float(c1[1])/float(c1[0]))
    r=round(r,3)
    a=round(a,3)
    coord=(r,a)
    return coord
