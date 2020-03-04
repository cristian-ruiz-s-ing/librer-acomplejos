import libreriacomplejos2 as lc2
import math

m=[[(0,0),(1/math.sqrt(2),0),(1/math.sqrt(2),0),(0,0)],
   [(1/math.sqrt(2),0),(0,0),(0,0),(-1/math.sqrt(2),0)],
   [(1/math.sqrt(2),0),(0,0),(0,0),(1/math.sqrt(2),0)],
   [(0,0),(-1/math.sqrt(2),0),(1/math.sqrt(2),0),(0,0)]]

w=[[(0.25, -0.25)], [(-0.25, -0.25)], [(-0.25, 0.75)], [(-0.25, 0.25)]]

m=lc2.daga(m)

v=lc2.multimatriz(m,w)
print(v)
