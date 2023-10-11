#Tiago Rodrigues Plum Ferreira GEC-1996
import numpy as np
#carregando um dataset

ds = np.loadtxt('paises.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

#1)
ds1 = ds[:,:4]
print(ds1)

#2)
ds2 = np.unique(ds[1:,1], return_counts=True)[0]
print(ds2)

#3)
ds3 = np.mean(ds[1:,-11].astype(np.float32))
print(ds3)

#4)
cond = np.char.find(ds[1:,1],'NORTHERN AMERICA') > -1
nort = np.array(ds[1:,1])[cond].shape[0]
print(nort)

#5)
cond = np.char.find(ds[1:,1],'LATIN AMER. & CARIB') > -1
cond2 = np.array(ds[1:,0])[cond]
maximo = np.max(np.array(ds[1:,8])[cond].astype(np.float32))
boolsaida = cond2[np.array(ds[1:,8])[cond].astype(np.float32) == maximo]
print(boolsaida)



