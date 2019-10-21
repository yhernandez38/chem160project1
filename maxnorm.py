import numpy as np
ntrials=5000
for i in range (1,201):
    sum=0
    for trial in range(ntrials):
        x=np.random.normal(size= i)
        x.sort()
        sum+=x[i-1]
    sum/=ntrials
print("N=",i,sum)