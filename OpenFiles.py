

n = 0

while True:
    
    f = open(f'file{n}',"w")
    n = str(n)
    f.write(n*100000)
    f.close()
    
    n = int(n)
    n = n+1
    
