def szybkiesort(lista):
    wieksze_rowne = []
    mniejsze = []
    if len(lista) > 1:
        pivot = lista[0]
        for liczba in lista[1:]:
            if liczba >= pivot:
                wieksze_rowne.append(liczba)
            else:
                mniejsze.append(liczba)
        return szybkiesort(wieksze_rowne) + [pivot] + szybkiesort(mniejsze)
    else:
        return lista

def unikalne(tekst):
     lista = []

     for znak in tekst:
        if znak not in lista:
             lista.append(znak)
     return lista


print(unikalne(szybkiesort(lista=[3,1,5,2,3,1,8])))


def wysz_znak(tekst):
    lista=[]
    for a in list(tekst):
        lista.append(tekst.count(a))
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            temp=i

    return tekst[temp]

print(wysz_znak("ala"))

def szukaj(liczba):
    slownik = {    "sto":1,
                   "dwiescie": 2,
                   "trzysta": 3,
                   "czterysta": 4,
                   "piencet": 5,
                   "szescset": 6,
                   "siedemset": 7,
                   "osiemset": 8,
                   "dziewiecet": 9,
                   "dziesiec":1,
                   "dwadziescia": 2,
                   "trzydziesci":3,
                   "czterdziesci":4,
                   "piedziesiat":5,
                   "szescdziesiąt":6,
                   "siedemdziesiat":7,
                   "osiemdziesiat": 8,
                   "dziewiedziesiat":9,
                   "zero":0,
                   "jeden": 1,
                   "dwa":2,
                   "trzy":3,
                   "cztery":4,
                   "piec":5,
                   "szejsc":6,
                   "siedem":7,
                   "osiem":8,
                   "dziewiec":9
                   }
    slowo=[]
    c=0

    for a in range(len(liczba)):
        
        if liczba[a]==" ":
            slowo.append(liczba[c:a])
            c=a+1
        if a==(len(liczba)-1):
            slowo.append(liczba[c:a+1])
            
    print(slowo)
    numer=[]

    for i in slowo:
        if i in slownik:
            numer.append(slownik[i])

    return numer


print(szukaj("dwiescie dwadziescia jeden"))