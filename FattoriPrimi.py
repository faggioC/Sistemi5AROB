import math

def isPrimo(n):
    div = int(math.sqrt(n)) + 1
    primo = True
    for i in range(2,div):
        if n % i==0:
            primo = False
            break
    
    return primo

def main():
    num = int(input("Inserisci un numero: "))
    f = open("numeriPrimi.txt", "r")
    listaPrimi = []
    righe = f.readlines()
    for riga in righe:
        listaPrimi.append(riga)


    divisori = []
    for i in listaPrimi:
        if num%int(i)==0:
            i = int(i)
            divisori.append(i)
    
    print(divisori)
if __name__ == "__main__":
    main()