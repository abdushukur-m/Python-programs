fibonachchi_sonlar = []

def fibonachchi_qaytar(son):
    f1 = 0
    f2 = 1
    fn = f1 + f2
    
    while True:
        if fn > son:
            break 
        fibonachchi_sonlar.append(fn)
        #print(f"{fn}", end=' ')
        fn = f1 + f2
        f1 = f2
        f2 = fn
        
    return son in fibonachchi_sonlar