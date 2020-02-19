import numpy as np
import matplotlib.pyplot as plt
import libreriacomplejos2 as lc2
#%matplotlib inline

v=[[(1,0)],[(0,0)],[(0,0)],[(0,0)]]
dinamica=[[(0,0),(0,0),(0,0),(0,0)],
          [(0,0),(0,0),(0,0),(1,0)],
          [(0,0),(1,0),(1,0),(0,0)],
          [(1,0),(0,0),(0,0),(0,0)]]

dinamica2=[[(0,0),(0.2,0),(0.3,0),(0.5,0)],
          [(0.3,0),(0.2,0),(0.1,0),(0.4,0)],
          [(0.4,0),(0.3,0),(0.2,0),(0.1,0)],
          [(0.3,0),(0.3,0),(0.4,0),(0,0)]]
clics=1
x=clics
while x>0:
    v=lc2.multimatriz(dinamica2,v)
    x-=1

print('Vector estado final: ',v)
labels=['pto. 0', 'pto. 1', 'pto. 2', 'pto. 3']
estado=[v[0][0][0], v[1][0][0], v[2][0][0], v[3][0][0]]

index =np.arange(len(labels))
#print('esto es index: ', index)
plt.bar(index,estado)
plt.xlabel('Estado')
plt.ylabel('valor')
plt.xticks(index, labels, rotation=75)
plt.title('Evolución dinámica del sistema después de '+str(clics)+' clics de tiempo')
plt.show()
