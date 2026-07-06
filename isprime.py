prime = []
isPrime = True 

for i in range(2,20):
    for n in i:
        if i % n == 0:
            isPrime = False
            break
        else:
            n+=1 
    