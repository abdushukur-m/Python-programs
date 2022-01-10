#5

def tubsonqaytar(son):
    tub_sonlar = []
    for n in range(2, son+1):
        k = 0    
        for m in range(1, n+1):
            if n % m == 0:
                k += 1
        if k == 2:
            tub_sonlar.append(n)
    return tub_sonlar

#print(tubsonqaytar(20))

#6
fibonacci_sonlar = []

def fibonachchi_qaytar(son):
    f1 = 0
    f2 = 1
    fn = 1
    while True:
        if fn > son:
            break 
        fibonacci_sonlar.append(fn)
        #print(f"{fn}", end=' ')
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return fibonacci_sonlar

print(fibonachchi_qaytar(50))
    


