#Zadania z egzaminu 
#Opracowane: Piotr Balcerzak

def quicksort(lista):
    wieksze_rowne = []
    mniejsze = []
    if len(lista) > 1:
        pivot = lista[0]
        for liczba in lista[1:]:
            if liczba >= pivot:
                wieksze_rowne.append(liczba)
            else:
                mniejsze.append(liczba)
        return quicksort(wieksze_rowne) + [pivot] + quicksort(mniejsze)
    else:
        return lista

def unikalne(tekst):
     lista = []

     for znak in tekst:
        if znak not in lista:
             lista.append(znak)
     return lista

print("Zad sorotwanie metoda quicksort oraz unikalne liczby")
print(unikalne(quicksort(lista=[3,1,5,2,3,1,8])))


def wysz_znak(tekst):
    lista=[]
    temp=' '
    for a in list(tekst):
        lista.append(tekst.count(a))
    for i in range(len(lista)-1):
        if lista[i]>lista[i + 1]:
            temp=tekst[i]


    return temp

print("Zad wyszukaj jaka litera powtarza sie najwiecej razy ")
print(wysz_znak("ziemniak z burakaa"))

def szukaj(liczba):
    slownik = {    "sto":100,
                   "dwiescie": 200,
                   "trzysta": 300,
                   "czterysta": 400,
                   "piencet": 500,
                   "szescset": 600,
                   "siedemset": 700,
                   "osiemset": 800,
                   "dziewiecet": 900,
                   "dziesiec":10,
                   "dwadziescia": 20,
                   "trzydziesci":30,
                   "czterdziesci":40,
                   "piedziesiat":50,
                   "szescdziesiąt":60,
                   "siedemdziesiat":70,
                   "osiemdziesiat": 80,
                   "dziewiedziesiat":90,
                   "jedenascie":11,
                   "dwanascie":12,
                   "trzynascie":13,
                   "czterascie":14,
                   "pietnascie":15,
                   "szesnascie":16,
                   "siedemnascie":17,
                   "osiemnascie":18,
                   "dziewietnascie":19,
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
            
    numer=0

    for i in slowo:
        if i in slownik:
            numer += slownik[i]

    return numer

print("Zad zamiana liczby slownej na cyfrowa")
print(szukaj("dwiescie dwadziescia jeden"))

def wysz(tekst,znak):
    liczba=0
    for a in list(tekst):
        if znak in a:
            liczba+=1

    return liczba

print("Zad wyszukaj ile razy powtarza sie litera w slowie")
zdanie="hakuna matata jak cudownie to brzmi"
print(zdanie)
print(wysz(zdanie,"a"))

def sort(tab): 
    for i in range(len(tab)):
        j=len(tab)-1 
        while j>i:   
            if tab[j]>tab[j-1]: 
                tmp=tab[j]
                tab[j]=tab[j-1]
                tab[j-1]=tmp
            j-=1

    return tab

print("Zad sortowanie bombelkowe")
print(sort([2,5,1,24,7]))
