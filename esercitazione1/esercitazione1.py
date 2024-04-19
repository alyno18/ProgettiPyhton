# Ex1: Scrivere un programma Python che elabora tre numeri e
# ne mostra in console:
#   La somma
#   La differenza
#   Il prodotto
#   Il valore medio
#   Il massimo
#   Il minimo

#a, b, c = input("Inserisci 3 numeri").split()
a = 6
b = 7
c = 8
print(a+b+c)
print(a-b-c)
print((a+b+c)/3)
print(max(a, b, c))
print(min(a, b, c))


# Ex2: Scrivere un programma Python che elabora un intero
# di 6 cifre e visualizza le singole cifre di cui è composto.
# Ad esempio, avendo il numero 458932,
# il programma deve visualizzare, su righe separate 4 5 8 9 3 2

num = 5678

for i in range(len(str(num))):
    print(str(num)[i])


# Ex3: Scrivere un programma che chiede all’utente di
# inserire una stringa e mostra a schermo se:
#   La stringa contiene almeno un numero
#   La stringa contiene tutte lettere minuscole
#   La stringa contiene soltanto numeri
#   La stringa contiene soltanto lettere e numeri

#stringa = input("Inserisci una stringa")
stringa = "ciao"

print(stringa.isdigit())
print(stringa.islower())
print(stringa.isupper())
print(stringa.isalnum())


# Ex4: Scrivere un programma Python che chiede all’utente
# di inserire quattro numeri e mostra in console la parola
# “crescenti” se sono in ordine strettamente crescente,
# “decrescenti” se sono in ordine strettamente decrescente e
# “nessuno dei due” se non sono né in ordine crescente
# né in ordine decrescente.

sequenza = []
n = int(input("Inserisci il numero di elementi che vuoi inserire"))
for i in range(0,n):
    ele = int(input("Inserisci un numero"))
    sequenza.append(ele)


# Ex5: Scrivere un programma Python che chiede all’utente di
# inserire un mese e un giorno e mostra in console
# la stagione dell’anno (Inverno, primavera, estate, autunno)
# relativa al mese e al giorno inseriti.

mese = int(input("Inserisci il mese"))
giorno = int(input("Inserisci il giorno"))

if (mese == 3 and giorno >= 20) or (mese == 6 and giorno <= 21) or (mese == 4) or (mese == 5):
    print("Primavera")
elif (mese == 6 and giorno >= 21) or (mese == 9 and giorno <= 22) or (mese == 7) or (mese == 8):
    print("Estate")
elif (mese == 9 and giorno >= 23) or (mese == 12 and giorno <= 21) or (mese == 10) or (mese == 11):
    print("Autunno")
elif (mese == 12 and giorno >= 22) or (mese == 3 and giorno <= 20) or (mese == 1) or (mese == 2):
    print("Inverno")
