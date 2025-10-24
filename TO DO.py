import os
import string
import time
import sys

def pulisci():
    os.system('clear')

def count():
    print("3...")
    time.sleep(2)
    pulisci()
    print("2...")
    time.sleep(2)
    pulisci()
    print("1...")
    time.sleep(2)
    pulisci()

def titolo():
    print("=========================TO DO LIST=====================================")


utente=input("inserisci nome utente: ")
if utente != "stefan" and utente!="nadia":
    print("nome utente non riconosciuto\n uscita dal programma...")
    sys.exit()
else:
    pulisci()
    print("benvenuto in TO DO LIST\n entrata nel programma...")
    count()
scelta=0

todos=["ciao", "ciaociao", "miaoooo"]

while scelta!=4:
    titolo()
    print("                  1. lista dei to do\n")
    print("                  2. crea nuovo to do\n")
    print("                  3. spunta un to do come fatto\n")
    print("                  4. esci da to do list\n")
    print("========================================================================\n")
    scelta_raw=input("inserisci valore: ")
    scelta=int(scelta_raw)
    pulisci()

    match scelta:
        case 1:
            titolo()
            print("                     lista dei to do:")
            for i in range(len(todos)):
                print(i+1,".", todos[i])

            skip=input("premere invio per tornare al menu\' iniziale...")
            pulisci()

        case 2:
            titolo()
            new=input("              inserisci nuovo to do: ")
            todos.append(new)
            if not new:
                skip=input("la stringa e\' vuota, premere invio per tornare al menu\' iniziale...")
            else: 
                skip=input("TO DO inserito correttamente!\npremi invio per tornare al menu\' iniziale\n")


        case 3:
            titolo()
            print("lista dei to do: \n")
            print("                     lista dei to do:")
            for i in range(len(todos)):
                print(i+1,".", todos[i])
            select_raw=input("digita il numero del to do da spuntare come già fatto: ")
            select=int(select_raw)
            del todos[select-1]
            q=input("premi invio per tornare al menu\' iniziale...")

        case 4:
            print("uscita dal programma...")
            time.sleep(2)
            sys.exit()

        case _:
            print("inserimento non valido...\n")
            time.sleep(2)
            print("uscita dal programma...")
            sys.exit()
