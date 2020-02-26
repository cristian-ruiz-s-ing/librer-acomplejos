import numpy as np
import matplotlib.pyplot as plt
import libreriacomplejos2 as lc2
#%matplotlib inline

#v=[[(0,0)],[(0,0)],[(1,0)],[(0,0)],[(0,0)],[(0,0)]]

dinamica=[[(0,0),(0,0),(0,0),(0,0)],
          [(0,0),(0,0),(0,0),(1,0)],
          [(0,0),(1,0),(1,0),(0,0)],
          [(1,0),(0,0),(0,0),(0,0)]]

dinamica2=[[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
          [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
          [(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)],
          [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
          [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
          [(1,0),(0,0),(0,0),(0,0),(1,0),(0,0)]]
total=4
clics=0

while clics<=total:
    v=[[(8,0)],[(2,0)],[(0,0)],[(4,0)],[(5,0)],[(10,0)]]
    x=clics
    while x>0:
        v=lc2.multimatriz(dinamica2,v)
        x-=1

    print('Vector estado final: ',v)
    labels=['pto. 0', 'pto. 1', 'pto. 2', 'pto. 3', 'pto. 4', 'pto. 5']
    estado=[v[0][0][0], v[1][0][0], v[2][0][0], v[3][0][0], v[4][0][0], v[5][0][0]]

    index =np.arange(len(labels))
    #print('esto es index: ', index)
    plt.bar(index,estado)
    plt.xlabel('Estado')
    plt.ylabel('valor')
    plt.xticks(index, labels, rotation=75)
    plt.title('Evolución dinámica del sistema después de '+str(clics)+' clics de tiempo')
    plt.show()
    clics+=1
    
