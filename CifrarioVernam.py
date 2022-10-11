import random
alfabeto = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"l":9,"m":10,"n":11,"o":12,"p":13,"q":14,"r":15,"s":16,"t":17,"u":18,"v":19,"z":20}
alfabetoContrario = {v: k for k, v in alfabeto.items()}
alfa = "abcdefghilmnopqrstuvz"
listaChiave = []



def generaChiave(chiave, lunghezza):
    c = ""
    if chiave == "random":
        for _ in range(lunghezza):
            c += alfa[random.randint(0,20)]
    else:
        c = chiave
    print(c)
    for i in c:
        listaChiave.append(alfabeto[i])
        
def codifica(parola):
    
    listaParola = []
    parolaCifrataN = []
    parolaCifrata = ""

    for i in parola:
        listaParola.append(alfabeto[i])

    for i in range(len(listaParola)):
        parolaCifrataN.append((listaChiave[i]+listaParola[i]) % 21)

    print(parolaCifrataN)
    for i in parolaCifrataN:
        parolaCifrata += alfabetoContrario[i]
    print(parolaCifrata)

def decodifica(parola):
    listaParola = []
    parolaCifrataN = []
    parolaCifrata = ""

    for i in parola:
        listaParola.append(alfabeto[i])

    for i in range(len(listaParola)):
        parolaCifrataN.append((listaParola[i] - listaChiave[i]) % 21)

    print(parolaCifrataN)
    for i in parolaCifrataN:
        parolaCifrata += alfabetoContrario[i]
    print(parolaCifrata)

def main():
    
    scelta = input("Codifica o Decodifica? [C/D]: ")
    scelta = scelta.upper()
    generaChiave(input("Inserisci chiave: "), 20)

    if scelta == "C":
        parola = input("Inserisci parola: ")
        
        codifica(parola)
    elif scelta == "D":
        parola = input("Inserisci parola: ")
        decodifica(parola)
    else:
        print("Scelta errata")


if __name__ == "__main__":
    main()




