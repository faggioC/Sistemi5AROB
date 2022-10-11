import math
nPrimi = []
f = open("numeriPrimi.txt", "w")

def isPrimo(n):
    div = int(math.sqrt(n)) + 1
    primo = True
    for i in range(2,div):
        if n % i==0:
            primo = False
            break
    
    return primo
            
            

def main():

    for i in range(2,10000000):
        if isPrimo(i):
            nPrimi.append(i)
            f.write(str(i) + "\n")
    
    print("fatto")

if __name__ == "__main__":
    main()