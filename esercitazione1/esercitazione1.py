# Ex1: Scrivere un programma Python che elabora tre numeri e ne mostra in console:
#   La somma, La differenza, Il prodotto, Il valore medio Il massimo Il minimo

#a, b, c = input("Inserisci 3 numeri").split()
a = 5
b = 6
c = 7
print(a+b+c)
print(a-b-c)
print((a+b+c)/3)
print(max(a, b, c))
print(min(a, b, c))


# Ex2: Scrivere un programma Python che elabora un intero di 6 cifre e visualizza le singole cifre di cui è composto.
# Ad esempio, avendo il numero 458932, il programma deve visualizzare, su righe separate 4 5 8 9 3 2

num = 5678

for i in range(len(str(num))):
    print(str(num)[i])


# Ex3: Scrivere un programma che chiede all’utente di inserire una stringa e mostra a schermo se:
#   La stringa contiene almeno un numero, La stringa contiene tutte lettere minuscole
#   La stringa contiene soltanto numeri, La stringa contiene soltanto lettere e numeri

#stringa = input("Inserisci una stringa")
stringa = "ciao"

print(stringa.isdigit())
print(stringa.islower())
print(stringa.isupper())
print(stringa.isalnum())


# Ex4: Scrivere un programma Python che chiede all’utente di inserire quattro numeri e mostra in console la parola
# “crescenti” se sono in ordine strettamente crescente, “decrescenti” se sono in ordine strettamente decrescente e
# “nessuno dei due” se non sono né in ordine crescente né in ordine decrescente.

num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))
num3 = float(input("Inserisci il terzo numero: "))
num4 = float(input("Inserisci il quarto numero: "))

if num1 > num2 > num3 > num4:
    print("Ordine strettamente decrescente")
elif num1 < num2 < num3 < num4:
    print("Ordine strettamente crescente")
else:
    print("la sequenza non è ne in ordine strettamente crescente ne in ordine strettamente decrescente")


# Ex5: Scrivere un programma Python che chiede all’utente di inserire un mese e un giorno e mostra in console
# la stagione dell’anno (Inverno, primavera, estate, autunno) relativa al mese e al giorno inseriti.

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


# Ex6: Scrivere un programma che chiede all’utente di inserire se è coniugato oppure no e il suo reddito e
# successivamente mostra in console le tasse dovute secondo lo schema nelle slide

reddito = float(input("Inserire il reddito: "))
coniugato = input("Coniugato o no? (inserire 1 o 0)")
tax = 0.0
if 10000 < reddito < 30000:
    if coniugato:
        tax = (reddito - 10000)*0.15
    else:
        tax = (reddito - 10000)*0.12
elif reddito > 30000:
    if coniugato:
        tax = (reddito - 30000)*0.35
    else:
        tax = (reddito - 30000)*0.30
print(tax)


# Ex7: Scrivere un programma Python che data una lista di numeri sostituisca ciascun valore con la media tra il valore
# stesso e i due adiacenti (o dell’unico valore adiacente se il valore in esame si trova all’estremità della lista).
# Scrivere due versioni del programma: una in cui i nuovi valori sono inseriti in una nuova lista e un’altra
# in cui i valori sono sostituiti direttamente nella lista di partenza.

def avg_same_list(data):

    if len(data) <= 1:
        return
    # Gestiamo il primo elemento della lista
    old_left = data[0]
    data[0] = (data[0] + data[1]) / 2
    # Gestiamo tutti gli elementi tranne l'ultimo
    for i in range(1, len(data) - 1):
        current = data[i]
        data[i] = (old_left + data[i] + data[i + 1]) / 3
        old_left = current

    # Gestiamo l'ultimo elemento della lista
    data[-1] = (old_left + data[len(data) - 1]) / 2


def avg_new_list(data):

    result = []

    # Gestiamo il primo elemento della lista
    result.append((data[0] + data[1]) / 2)

    # Gestiamo tutti gli elementi tranne l'ultimo
    for i in range(1, len(data) - 1):
        value = (data[i - 1] + data[i] + data[i + 1]) / 3
        result.append(value)

    # Gestiamo l'ultimo elemento della lista
    result.append((data[-2] + data[-1]) / 2)

    return result


values = [1, 2, 3, 5, 3, 1, 4]
print("I valori originali sono: ", values)

smoothed_alternative = avg_new_list(values)
print("I valori mediati su una nuova lista sono: ", smoothed_alternative)

avg_same_list(values)
print("I valori mediati sono: ", values)


# Ex: Scrivere un programma Python per gestire la prenotazione di posti in uno stadio. Assumere che i posti siano
# organizzati come una matrice rettangolare in cui il numero contenuto indicail prezzo del posto,
# oppure il numero -1 se il posto è già occupato.
# Il programma deve chiedere all’utente di scegliere un posto inserendo un indice di riga e di colonna,
# oppure di inserire un prezzo.
# Quando l’utente specifica un posto, il programma deve verificare che il posto sia libero e visualizzare un messaggio
# che segnala che la prenotazione è andata a buon fine mostrando il prezzo,
# oppure un messaggio che segnala che il post è occupato.
# Se l’utente sceglie il prezzo, il programma deve assegnare un posto tra i disponibili (se presenti) e visualizzare
# l’indice di riga e colonna del posto assegnato.
# Una volta terminata l’interazione, il programma torna in attesa del prossimo input da parte dell’utente

# Inizializziamo il prezzo dei posti.
price_chart = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
               [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
               [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
               [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
               [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
               [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
               [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
               [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
               [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]]

# Input utente
choice = input("Scegli un Posto (S), un Prezzo (P) o Esci (E)? ").upper()
while choice != "E":
    # Gestiamo il caso in cui l'utente vuole scegliere il posto
    if choice == "S":
        row = int(input("Inserire la riga: "))
        col = int(input("Inserire la colonna: "))
        # Verifichiamo se è disponibile.
        if price_chart[row][col] != -1:
            print(f"Prenotato al prezzo di {price_chart[row][col]}!")
            price_chart[row][col] = -1
        else:
            print("Purtroppo il posto è già occupato.")
    # Gestiamo il caso in cui l'utente sceglie un prezzo.
    elif choice == "P":
        price = float(input("Quanto vuole spendere?"))
        found = False

        for row in range(len(price_chart)):
            for col in range(len(price_chart[row])):
                if price_chart[row][col] == price and not found:
                    print(f"E' disponibile il posto ({row}, {col}) ed è stato prenotato!")
                    price_chart[row][col] = -1
                    found = True
                    break
            if found:
                break
        if not found:
            print("Non ci sono posti disponibili al prezzo indicato.")
    else:
        print("Non è un opzione valida.")

    # Input per la scelta successiva.
    choice = input("Scegli un Posto (S), un Prezzo (P) o Esci (E)?").upper()

for row in range(len(price_chart)):
    for col in range(len(price_chart[row])):
        print(f"{price_chart[row][col]:3d}", end="")
    print()
