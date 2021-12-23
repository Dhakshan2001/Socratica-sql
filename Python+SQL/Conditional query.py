import psycopg2 as psc 
import numpy as np
from numpy import genfromtxt

def query(star,planet):
    a = genfromtxt(star, delimiter=',')
    b = genfromtxt(planet, delimiter=',')
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i,0] == b[j,0] and a[i,2] > 1:
                d = [b[j,5]/a[i,2]]
                c.append(d)
    d = np.asarray(c)
    op = d[np.argsort(d[:, 0])]
    return op
