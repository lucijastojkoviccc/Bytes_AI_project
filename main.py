import os
import sys
import copy
from timeit import default_timer as timer
from datetime import timedelta
import random
from collections import deque



def ispisi_veliku_tablu(tabla):
    columns_labels = '   ' + '  '.join([' ' * 2 + str(i + 1) + ' ' * 2 for i in range(velicina_vece_table)])
    print(columns_labels)

    for row_index, row in enumerate(tabla):
        row_label = chr(ord('A') + row_index)

        for i in range(3):
            print(row_label if i == 1 else ' ', end='  ')
            for small_table in row:
                print(' '.join(small_table[i]), end='  ')
            print()
        print()
def kreiraj_malu_tablu_t():
    return [['.' for _ in range(3)] for _ in range(3)]
def kreiraj_malu_tablu_b():
    return [[' ' for _ in range(3)] for _ in range(3)]
def pristupi_specificnoj_tacki(row, column, char, placeX, placeY):
    specific_small_table = velika_tabla[row][column]
    specific_small_table[placeX][placeY] = char
def pocetnoStanje():
    # CRNO - X
    for x in range(2, velicina_vece_table, 2):
        for y in range(2, velicina_vece_table + 1, 2):
            a=2
            pristupi_specificnoj_tacki(int(x - 1), int(y - 1), 'X', 0, 0)

    # ZA PROVERE
    pristupi_specificnoj_tacki(1, 1, 'X', 0, 0)
    pristupi_specificnoj_tacki(1, 1, 'X', 0, 1)



    pristupi_specificnoj_tacki(3, 1, 'X', 0, 0)
    pristupi_specificnoj_tacki(3, 1, 'X', 0, 1)

    pristupi_specificnoj_tacki(3, 1, 'X', 0, 2)
    pristupi_specificnoj_tacki(3, 1, 'X', 1, 0)

    pristupi_specificnoj_tacki(3, 1, 'X', 1, 1)
    #pristupi_specificnoj_tacki(1, 1, 'X', 1, 2)

    # pristupi_specificnoj_tacki(0, 0, 'O', 1, 0)
    #
    # # pristupi_specificnoj_tacki(0, 0, 'X', 0, 2)
    # # pristupi_specificnoj_tacki(0, 2, 'X', 0, 0)
    # # pristupi_specificnoj_tacki(0, 2, 'X', 0, 1)
    # # pristupi_specificnoj_tacki(0, 2, 'X', 0, 2)
    # #
    # #
    # #
    # # pristupi_specificnoj_tacki(0, 0, 'X', 1, 0)


    pristupi_specificnoj_tacki(2, 2, 'X', 0, 1)


    # pristupi_specificnoj_tacki(2, 6, 'X', 0, 1)
    #
    pristupi_specificnoj_tacki(1, 1, 'X', 0, 2)
    pristupi_specificnoj_tacki(1, 1, 'X', 1, 0)
    # # pristupi_specificnoj_tacki(0, 0, 'X', 0, 0)
    # # pristupi_specificnoj_tacki(0, 0, 'X', 0, 1)
    pristupi_specificnoj_tacki(1, 1, 'X', 1, 1)
    # # pristupi_specificnoj_tacki(4, 4, 'X', 0, 0)
    # # pristupi_specificnoj_tacki(4, 6, 'X', 0, 0)
    # pristupi_specificnoj_tacki(4, 4, 'O', 0, 0)
    # pristupi_specificnoj_tacki(4, 0, 'O', 0, 2)
    # pristupi_specificnoj_tacki(4, 0, 'O', 1, 0)
    # pristupi_specificnoj_tacki(6, 2, 'O', 0, 1)
    # pristupi_specificnoj_tacki(6, 2, 'O', 0, 2)
    # pristupi_specificnoj_tacki(6, 2, 'O', 1, 0)
    # pristupi_specificnoj_tacki(2, 4, 'X', 0, 0)
    #
    # pristupi_specificnoj_tacki(6, 4, 'X', 0, 0)

    # BELO - O
    for x in range(3, velicina_vece_table, 2):
        for y in range(1, velicina_vece_table, 2):
            a=2
            pristupi_specificnoj_tacki(int(x - 1), int(y - 1), 'O', 0, 0)


def podesavanje_igre():
    print("Izaberite opciju:")
    print("1 - Drugi igrac")
    print("2 - Kompjuter")

    while True:
        try:
            choice = int(input("Izaberi opciju (1 ili 2): "))
            if choice in [1, 2]:
                break
            else:
                print("Izbor nije validan. Izaberite 1 ili 2.")
        except ValueError:
            print("Izbor nije validan. Unesite broj")

    if choice == 1:
        order = input("Da li zelite da igrate prvi ili drugi (Unesite 1 ili 2): ").lower()
        while order not in ['1', '2']:
            print("Izbor nije validan. Unesite 1 ili 2")
            order = input("Da li zelite da igrate prvi ili drugi? ").lower()
    else:
        order = input("Da li zelite da igrate prvi ili drugi (Unesite 1 or 2): ").lower()
        print(f"Vi cete igrati {order}.")

    return (choice, order)


def potez_validan(rowNext, colNext, rowCurr, colCurr):
    if rowNext < 0 or rowNext >= len(velika_tabla) or colNext < 0 or colNext >= len(velika_tabla[0]):
        print("Izabrano polje se ne nalazi na tabli!")
        return False
    #  Da li se krecemo dijagonalno i da li se krecemo za samo jedno polje
    if abs(rowNext - rowCurr) != abs(colNext - colCurr) and abs(rowNext - rowCurr) != 1 and abs(colNext - colCurr) != 1:
        print("Izabrano polje nije u dometu!")
        return False
    # Da li je polje na koje zelimo da odemo crno
    if velika_tabla[rowNext][colNext][1][1] == ' ':
        print("Dozvoljeno je kretati se samo po crnim poljima table.")
        return False
    return True


def najkraca_putanja(trenutni_red, trenutni_kol, ciljni_red, ciljni_kol):
    redovi = len(velika_tabla)
    kolone = len(velika_tabla[0])

    def validno_polje(red, kol):
        return 0 <= red < redovi and 0 <= kol < kolone and velika_tabla[red][kol][1][1] == '.'

    # Inicijalizacija reda za BFS
    red = deque([(trenutni_red, trenutni_kol, [])])

    # Set za praćenje posećenih polja
    posecena_polja = set()

    while red:
        trenutno_polje = red.popleft()
        trenutni_red, trenutni_kol, putanja = trenutno_polje

        if (trenutni_red, trenutni_kol) == (ciljni_red, ciljni_kol):
            # Ako smo stigli do ciljnog polja, vraćamo putanju
            return putanja

        if (trenutni_red, trenutni_kol) not in posecena_polja:
            posecena_polja.add((trenutni_red, trenutni_kol))

            # Susedna polja
            susedi = [
                (trenutni_red - 1, trenutni_kol - 1),  # gore-levo
                (trenutni_red - 1, trenutni_kol + 1),  # gore-desno
                (trenutni_red + 1, trenutni_kol - 1),  # dole-levo
                (trenutni_red + 1, trenutni_kol + 1),  # dole-desno
            ]

            for sused in susedi:
                red_sused, kol_sused = sused
                if validno_polje(red_sused, kol_sused):
                    red.append((red_sused, kol_sused, putanja + [(red_sused, kol_sused)]))

    return []

def nadji_najblizeg_suseda_sa_figurama(tabla,row, col):
    distance = 0
    min_distance = 2 * velicina_vece_table
    closest_neighbors = []

    while True:
        distance += 1
        found_valid_neighbor = False
        current_neighbors = []

        for i in range(-distance, distance + 1):
            for j in range(-distance, distance + 1):
                if i != 0 or j != 0:
                    neighbor_row, neighbor_col = row + i, col + j
                    if ima_figura_u_polju(velika_tabla,neighbor_row, neighbor_col):
                        current_neighbors.append((neighbor_row, neighbor_col))
                        found_valid_neighbor = True

        if found_valid_neighbor:
            if min_distance is None or distance < min_distance:
                min_distance = distance
                closest_neighbors = current_neighbors

        if min_distance and distance > min_distance:
            return closest_neighbors

def ima_figura_u_polju(tabla, rowCurr, colCurr):
    if(rowCurr<0 or rowCurr>=velicina_vece_table or colCurr<0 or colCurr>=velicina_vece_table):
        return False
    for row in tabla[rowCurr][colCurr]:
        for small_table_row in row:
            for elem in small_table_row:
                if elem != '.' and elem !=' ':
                    return True
    return False  #znaci da je prazna




def okolna_polja_prazna(tabla,row, col):
    if (row == 0): #prvi red
        if (col == 0):
            if ((ima_figura_u_polju(tabla,row + 1, col + 1) == False)): return True
        if (col >= 2 and col + 1 < velicina_vece_table):
            if ((ima_figura_u_polju(tabla,row + 1, col - 1) == False) and (ima_figura_u_polju(tabla,row + 1, col + 1) == False)): return True

    if (row == velicina_vece_table - 1): #poslednji red
        if (col == velicina_vece_table - 1):
            if ((ima_figura_u_polju(tabla,row - 1, col - 1) == False)): return True
        if (col >= 1 and col + 2 < velicina_vece_table):
            if ((ima_figura_u_polju(tabla,row - 1, col - 1) == False) and (ima_figura_u_polju(tabla,row - 1, col + 1) == False)): return True

    if(col==0): #prva kolona
        if(row>=2 and row+1<velicina_vece_table):
            if ((ima_figura_u_polju(tabla,row - 1, col + 1) == False) and (ima_figura_u_polju(tabla,row + 1, col + 1) == False)): return True

    if(col==velicina_vece_table-1): #poslednja kolona
        if (row >= 1 and row + 2 < velicina_vece_table):
            if ((ima_figura_u_polju(tabla,row - 1, col - 1) == False) and (ima_figura_u_polju(tabla,row + 1, col - 1) == False)): return True


    if(row+1<velicina_vece_table and col+1<velicina_vece_table and row-1>=0 and col-1>=0): #nije nista od ovog navedenog
        if((ima_figura_u_polju(tabla,row+1, col+1)==False) and (ima_figura_u_polju(tabla,row + 1, col - 1) == False) and (ima_figura_u_polju(tabla,row - 1, col + 1) == False) and (ima_figura_u_polju(tabla,row - 1, col - 1) == False)):
            print("Sva polja oko izabranog su prazna")
            return True

    return False

def potencijalni_potezi(tabla,row, col):
    print("Potencijalni potezi:", end=" ")
    if(ima_figura_u_polju(tabla,row - 1, col - 1) and row-1>=0 and col-1>=0):
        print("GL", end=" ")
    if(ima_figura_u_polju(tabla,row - 1, col + 1) and row-1>=0 and col+1<velicina_vece_table):
        print("GD", end=" ")
    if (ima_figura_u_polju(tabla,row + 1, col - 1)and row+1<velicina_vece_table and col-1>=0):
        print("DL", end=" ")
    if (ima_figura_u_polju(tabla,row + 1, col + 1) and row+1<velicina_vece_table and col+1<velicina_vece_table ):
        print("DD", end=" ")

def remove_figures_from_matrix(tabla,RedC,KolonaC, figure_index, brRedova, brKolona, trIgrac, poz0, poz1):
    matrix = tabla[RedC][KolonaC]

    figure_index = figure_index - 1
    if figure_index < 0 or figure_index > 7:
        raise ValueError("Izabrati vrednost izmedju 1 i 8")
    visina = 0
    for i in range(brRedova):
        for j in range(brKolona):
            if (matrix[i][j] != '.'):
                visina = visina + 1
    brojac = 0
    arr = []
    count = sum(1 for row in tabla[poz0][poz1] for small_table_row in row for elem in small_table_row if
                elem != '.')
    for i in range(brRedova):
        for j in range(brKolona):
            I = copy.deepcopy(i)
            J = copy.deepcopy(j)
            #print(matrix)
            if (brojac != figure_index):

                brojac = brojac + 1
            else:
                #if (trIgrac == matrix[i][j]):
                for k in range(i, brRedova, 1):
                        for m in range(j, brKolona, 1):
                            if (matrix[k][m] != '.'):
                                arr.append(matrix[k][m])
                            if (m == brKolona - 1):
                                j = 0

                okolina_polja = okolna_polja_prazna(tabla,RedC,KolonaC)
                if(okolina_polja == True):
                    for k in range(I, brRedova):
                        for m in range(J, brKolona):
                            matrix[k][m] = '.'
                    break
                else:

                    if (8 - count) >= len(arr):
                        if visina < (len(arr) + count):
                            for k in range(I, brRedova):
                                for m in range(J, brKolona):
                                    matrix[k][m] = '.'
                            break
                        else:
                            raise ValueError("Drugi stek će imati manji broj figura, mora da ih ima više")
                    else:
                        raise ValueError("Nema dovoljno mesta u steku")

        #print(matrix)
        #print(arr)

    return arr



def reset_mala(mala):
    for i in range(3):
        for j in range(3):
            if(mala[i][j] != "."):
                mala[i][j] = "."


def pobedio(n,p):
    ukupanBrojStekova = int((n - 2) * (n / 2) / 8)
    if(p == "O"):
        global stekO

        stekO = stekO + 1

    if (p == "X"):
        global stekX

        stekX = stekX + 1


    if (stekX > stekO and (stekX >= (ukupanBrojStekova + 1) // 2)):
        print("Igrac broj 1 je pobedio")
        print("IGRA JE ZAVRSENA")
        sys.exit()
        #return True
    elif (stekX < stekO and (stekO >= (ukupanBrojStekova // 2))):
        print("Igrac broj 2 je pobedio")
        print("IGRA JE ZAVRSENA")
        sys.exit()
        #return True

    count = [sum(1 for row in matrix for elem in row if elem != '.') for matrix in velika_tabla]
    total_count = sum(count)
    if (total_count == 0):
        print("IGRA JE ZAVRSENA")
        sys.exit()
        #return True

   # return False


def provera_male_matrice(mala):

    b = 0
    for i in range(3):
        for j in range(3):
            if(mala[i][j] != "."):
                b = b+1
    return b


def provera_boje(tr,mesto,mala_mat):
    b = 1
    for i in range(3):
        for j in range(3):
            if(b == mesto):
                if(mala_mat[i][j] == tr):
                    return 1
                else:
                    raise ValueError("Ne valja boja.")

            else:
                b = b+1

def unos_poteza(trenutni_igrac):
    while True:
        try:
            pozicija = input("Unesite poziciju polja (npr. A1): ").upper()
            kolona_broj=None
            if len(pozicija)==2:
                if(pozicija[0].isalpha() and pozicija[1].isdigit()):
                    kolona_broj = abs(int(pozicija[1]) - 1)

                else: raise ValueError("Neispravan unos za poziciju.")
            elif len(pozicija)==3:
                if (pozicija[0].isalpha() and pozicija[1].isdigit() and pozicija[2].isdigit()):
                    kb1= abs(int(pozicija[1]))
                    kb2=abs(int(pozicija[2]))
                    spojeno = str(kb1) + str(kb2)
                    kolona_broj=abs(int(spojeno)-1)
                    # print("Kolona:", kolona_broj)
                else:
                    raise ValueError("Neispravan unos za poziciju.")
            else:
                raise ValueError("Neispravan unos za poziciju.")
            red_slovo=pozicija[0]
            # Pretvaranje reda u indeks
            red_broj = ord(red_slovo) - ord('A')
            #trenutno izabrano polje da nije nesto sto nije na tabeli
            if (kolona_broj > velicina_vece_table or red_broj > velicina_vece_table):
                raise ValueError("Neispravan unos za poziciju.")
            #trenutno izabrano polje da nije prazno
            if not (ima_figura_u_polju(velika_tabla, red_broj, kolona_broj)):
                raise ValueError("Izabrana pocetna pozicija nema figure.")
            # Da li je polje sa kojeg polazimo crno
            if velika_tabla[red_broj][kolona_broj][1][1] == ' ':
                print("Dozvoljeno je kretati se samo po crnim poljima table.")
                raise ValueError("Neispravan unos za poziciju.")


            figura_mesto=None
            redNext = None
            kolNext = None
            flag = 0
            #provera da nisu sva okolna polja oko naseg polja prazna
            okolina_prazna=okolna_polja_prazna(velika_tabla, red_broj, kolona_broj)
            #ako je okolina prazna da se pravi funkcija koja proverava najkraci put do sledeceg polja koje nije prazno
            if(okolina_prazna):
                flag = 1
                result = nadji_najblizeg_suseda_sa_figurama(velika_tabla,red_broj, kolona_broj)
                if result is not None:
                    putanja = []
                    for i in range(0, len(result)):
                        rezultati = result[i]
                        putanja.append(najkraca_putanja(red_broj, kolona_broj, rezultati[0], rezultati[1]))
                    print("Putanje do najblizih stekova: ")
                    print(putanja)

                    print("Najblizi stekovi su na pozicijama:", end=" ")
                    for x in result:
                        rn, cn = x  #ovo su red next i col next iz putanje

                        row_label = chr(ord('A') + rn)
                        print(row_label,cn+1," ", end=" ")
                    print("\n")

                else:
                    print("Result je nun")
                    return

            mala_matrica = velika_tabla[red_broj][kolona_broj]

            figura_mesto = int(input("Unesite mesto figure na steku koju pomerate (ceo broj): "))
            provera_boje(trenutni_igrac,figura_mesto,mala_matrica)
            potencijalni_potezi(velika_tabla, red_broj, kolona_broj)

            smer = input("\nUnesite smer pomeranja (GL, GD, DL, DD): ").upper()
            redCurr = red_broj
            kolCurr = kolona_broj
            if smer not in ['GL', 'GD', 'DL', 'DD']:
                raise ValueError("Neispravan unos za smer pomeranja.")
            if smer == 'GL':
                redNext = red_broj - 1
                kolNext = kolona_broj - 1
            if smer == 'GD':
                redNext = red_broj - 1
                kolNext = kolona_broj + 1
            if smer == 'DL':
                redNext = red_broj + 1
                kolNext = kolona_broj - 1
            if smer == 'DD':
                redNext = red_broj + 1
                kolNext = kolona_broj + 1

            #PROVERA DA LI SE KRECEMO DOBROM PUTANJOM
            if(flag == 1):
                def trenutna_pozicija_u_putanjama(trenutna_pozicija, lista_putanja):
                    for putanja in lista_putanja:
                        if trenutna_pozicija in putanja:
                            return True
                    return False
                trenutna_pozicija = (redNext, kolNext)

                if trenutna_pozicija_u_putanjama(trenutna_pozicija, putanja):
                    print(f"Trenutna pozicija {trenutna_pozicija} se krece ka jednom od najblizih stekova.")
                else:
                    raise ValueError(f"Trenutna pozicija {trenutna_pozicija} se ne krece ka jednom od najblizih stekova.")


            if (potez_validan(redNext, kolNext, redCurr, kolCurr) is True):
                niz = remove_figures_from_matrix(velika_tabla,red_broj,kolona_broj, figura_mesto, 3, 3, trenutni_igrac, redNext, kolNext)
            else:
                raise ValueError("Pokusaj opet! Ne smes van table!")
            if(niz == False):
                raise ValueError("Ne valja niz")

            mala_matrica = velika_tabla[redNext][kolNext]
            if (potez_validan(redNext, kolNext, redCurr, kolCurr)):
                niz_izbacenih = niz
                #pred_visina = niz[1]

                k = 0
                for i in range(3):
                    for j in range(3):
                        if (mala_matrica[i][j] == '.'):
                            mala_matrica[i][j] = niz_izbacenih[k]
                            k = k + 1
                            if (k == len(niz_izbacenih)):
                                print(mala_matrica)
                                pr = provera_male_matrice(mala_matrica)
                                if(pr == 8):
                                    poslednji = mala_matrica[2][1]
                                    pobedio(velicina_vece_table,poslednji)
                                    reset_mala(mala_matrica)
                                if(trenutni_igrac == 'X'):
                                    return 'O'
                                else:
                                    return 'X'

                                #return 0

        except ValueError as e:
            print(f"Greška pri unosu poteza: {e}")
            return None
def igrajZaStanja(kljuc,lista_poteza):


    # print(potez)
    # kljuc mu dodje nova mala matrica na koju ide, a lista poteza zapravo figura koju pomera
    # print(nova_stanja(len(velika_tabla), trenutni_igrac))
    # print(f"Najbolji potez: {kljuc} - {lista_poteza}")



    trenutniRed, trenutnaKol, vrh, preostaloMesta = kljuc
    okolina_prazna = okolna_polja_prazna(velika_tabla, trenutniRed, trenutnaKol)
    lista_fush=[]
    for r in lista_poteza:
        fush_tabla = copy.deepcopy(velika_tabla)
        noviRed, novaKol, trenutnoMestoFigureNaSteku, mestaZaNove = r

        niz = remove_figures_from_matrix(fush_tabla, trenutniRed, trenutnaKol, trenutnoMestoFigureNaSteku, 3, 3, trenutni_igrac,
                                     noviRed, novaKol)
        # E SAD IH PREBACIMO
        mala_matrica = fush_tabla[noviRed][novaKol]
        if (potez_validan(noviRed, novaKol, trenutniRed, trenutnaKol)):
            niz_izbacenih = niz
            k = 0
            napusti_petlje = False

            for i in range(3):
                for j in range(3):
                    if mala_matrica[i][j] == '.':
                        mala_matrica[i][j] = niz_izbacenih[k]
                        k += 1

                        if k == len(niz_izbacenih):
                            # print(mala_matrica)
                            pr = provera_male_matrice(mala_matrica)

                            if pr == 8:
                                poslednji = mala_matrica[2][1]
                                pobedio(velicina_vece_table, poslednji)
                                reset_mala(mala_matrica)

                            napusti_petlje = True
                            break  # Izlazimo iz unutrašnje for petlje

                if napusti_petlje:
                    break
                # ispisi_veliku_tablu(fush_tabla)
        lista_fush.append(fush_tabla)
    return lista_fush

def generisiSvaStanja(velicina_vece_table):
    poteziX=nova_stanja(velicina_vece_table,"X")
    poteziO=nova_stanja(velicina_vece_table, "O")
    poteziX.update(poteziO)
    svaStanja=[]
    for key,value in poteziX.items():
        stanjce=igrajZaStanja(key,value)
        # print("AAA")
        # print(stanjce)
        # for x in stanjce:
        #     ispisi_veliku_tablu(x)
        # svaStanja.append(stanjce)

    return svaStanja

def nova_stanja(velicina_vece_table,boja):
    stanja = {}
    for i in range(velicina_vece_table):
        for j in range(velicina_vece_table):
            mala = velika_tabla[i][j]
            p = 0
            trenutni=None
            brojac=0
            for x in range(3):
                for y in range(3):
                    if(mala[x][y]=='.'):
                        break
                    brojac=brojac+1
                    trenutni=mala[x][y]
            if (i + j) % 2 == 0:
                brT = provera_male_matrice(velika_tabla[i][j])

                if brT == 0:
                    continue
                potezi = generisi_poteze(i, j, velicina_vece_table)
                if potezi.values() == 0:
                    continue
                P = list(potezi.values())

                stajeGL = 0
                stajeGD = 0
                stajeDL = 0
                stajeDD = 0
                if okolna_polja_prazna(velika_tabla,i,j):
                    result = nadji_najblizeg_suseda_sa_figurama(velika_tabla, i, j)
                    if result is not None:
                        putanja = []
                        for m in range(3):
                            for n in range(3):
                                if (mala[m][n] == '.'):
                                    break

                                k = p + 1
                                p = p + 1
                                prebacuje = brT + 1 - p
                        for q in range(0, len(result)):
                            rezultati = result[q]
                            putanja.append(najkraca_putanja(i, j, rezultati[0], rezultati[1]))
                            for z in putanja:
                               # print(z[0])
                                skok = z[0]
                                kljucL = [i, j, trenutni, p, prebacuje]
                                kljuc = tuple(kljucL)
                                broooj = provera_male_matrice(velika_tabla[skok[0]][skok[1]])
                                dozvoljenoooo = 8 - broooj
                                l = [skok[0], skok[1], dozvoljenoooo]
                                stanja.setdefault(kljuc, []).append(l)
                else:

                    if 'GL' in P[0]:
                        brGL = provera_male_matrice(velika_tabla[i-1][j-1])
                        dozvoljenoGL = 8 - brGL
                        stajeGL = brT - dozvoljenoGL

                        if brGL == 0:
                            stajeGL = 9

                        if stajeGL < 0:
                            stajeGL = 0

                    if 'GD' in P[0]:

                        brGD = provera_male_matrice(velika_tabla[i - 1][j + 1])
                        dozvoljenoGD = 8 - brGD
                        stajeGD = brT - dozvoljenoGD

                        if brGD == 0:
                            stajeGD = 9

                        if stajeGD < 0:
                            stajeGD = 0

                    if 'DL' in P[0]:

                        brDL = provera_male_matrice(velika_tabla[i + 1][j - 1])
                        dozvoljenoDL = 8 - brDL
                        stajeDL = brT - dozvoljenoDL

                        if brDL == 0:
                            stajeDL = 9

                        if stajeDL < 0:
                            stajeDL = 0

                    if 'DD' in P[0]:

                        brDD = provera_male_matrice(velika_tabla[i + 1][j + 1])
                        dozvoljenoDD = 8 - brDD
                        stajeDD = brT - dozvoljenoDD

                        if brDD == 0:
                            stajeDD = 9

                        if stajeDD < 0:
                            stajeDD = 0

                for m in range(3):
                    for n in range(3):
                        if(mala[m][n] == '.' ):
                            break

                        k = p + 1
                        p = p + 1
                        prebacuje = brT + 1 - p

                        if 'GL' in P[0] and k > stajeGL and (brT < prebacuje + brGL) and boja == mala[m][n]:
                            kljucL = [i, j, trenutni, p, prebacuje]
                            kljuc = tuple(kljucL)

                            l = [i - 1, j - 1, dozvoljenoGL]
                            stanja.setdefault(kljuc, []).append(l)
                        if 'DL' in P[0] and k > stajeDL and (brT < prebacuje + brDL) and boja == mala[m][n]:
                            kljucL = [i, j, trenutni, p, prebacuje]
                            kljuc = tuple(kljucL)

                            l = [i + 1, j - 1, dozvoljenoDL]
                            stanja.setdefault(kljuc, []).append(l)
                        if 'DD' in P[0] and k > stajeDD and (brT < prebacuje + brDD) and boja == mala[m][n]:
                            kljucL = [i, j, trenutni, p, prebacuje]
                            kljuc = tuple(kljucL)
                            l = [i + 1, j + 1, dozvoljenoDD]
                            stanja.setdefault(kljuc, []).append(l)
                        if 'GD' in P[0] and k > stajeGD and (brT < prebacuje + brGD) and boja == mala[m][n]:
                            kljucL = [i, j, trenutni, p, prebacuje]
                            kljuc = tuple(kljucL)
                            l = [i - 1, j + 1, dozvoljenoGD]
                            stanja.setdefault(kljuc, []).append(l)

    return stanja

def generisi_poteze(row,col,velicina_vece_table):
    kljucL = [row,col]
    kljuc = tuple(kljucL)
    moguci_potezi = {}


    if row - 1 >= 0 and col - 1 >= 0 and (provera_male_matrice(velika_tabla[row - 1][col - 1]) != 0):
        moguci_potezi.setdefault(kljuc, []).append("GL")
    if row + 1 < velicina_vece_table and col - 1 >= 0 and (provera_male_matrice(velika_tabla[row + 1][col - 1]) != 0):
        moguci_potezi.setdefault(kljuc, []).append("DL")
    if row - 1 >= 0 and col + 1 < velicina_vece_table and (provera_male_matrice(velika_tabla[row - 1][col + 1]) != 0):
        moguci_potezi.setdefault(kljuc, []).append("GD")
    if row + 1 < velicina_vece_table and col + 1 < velicina_vece_table and (provera_male_matrice(velika_tabla[row + 1][col + 1]) != 0):
        moguci_potezi.setdefault(kljuc, []).append("DD")
    if moguci_potezi == {}:
        moguci_potezi.setdefault(kljuc, []).append("Prazno")


    return moguci_potezi

###### ODAVDEEE NADALJE RADILA ZA MINMAX KONKRETNO
def proceni_stanje(igrac, stanje):  #heuristikaaa
    # Implementiraj funkciju za procenu stanja koristeći pravila zaključivanja
    # Ova funkcija treba da vrati numeričku vrednost koja predstavlja ocenu stanja
    # Što je veća vrednost, to je stanje bolje za trenutnog igrača
    # Ako je vrednost pozitivna, trenutni igrač ima prednost, a ako je negativna, protivnik ima prednost
    # Možeš koristiti mašinu za zaključivanje i definisati pravila za ocenjivanje stanja

    # x=igra_je_zavrsena(velicina_vece_table)
    # if(x):
    #     if(stekO>stekX):
    #         return "O"
    #     elif(stekX>stekO):
    #         return "X"
    #     else:
    #         return "Nereseno"
    if (igrac == "O"):
        return stekO

    else:
        return stekX


    #return len([figura for red in stanje for mala_matrica in red for figura in mala_matrica if figura == igrac])
    #samo demonstracija za pocetak

def igra_je_zavrsena(tabla):
        n = len(tabla)
        ukupanBrojStekova = int((n - 2) * (n / 2) / 8)
        if (stekX > stekO and (stekX >= (ukupanBrojStekova + 1) // 2)):
            return True
        elif (stekX < stekO and (stekO >= (ukupanBrojStekova // 2))):
            return True
        count = [sum(1 for row in matrix for elem in row if elem != '.') for matrix in velika_tabla]
        total_count = sum(count)
        if (total_count == 0):
           return True

        return False


def promeni_igraca(igrac):
    return 'O' if igrac == 'X' else 'X'

#OVO KAZE GPT ZA HEURISTIKU ALI MI NIJE JASNA

#U funkciji heuristika trebaš implementirati svoju heuristiku koja ocenjuje
# trenutno stanje igre. Heuristika bi trebalo da vrati neku numeričku vrednost
# koja predstavlja procenu stanja. Ova vrednost će se koristiti u Min-Max algoritmu
# umesto dubine prilikom ocenjivanja stanja tokom pretrage stabla igre.

def minmax_alpha_beta(igrac, stanje, dubina, alfa, beta):
    if dubina == 0 or igra_je_zavrsena(velika_tabla):
        return proceni_stanje(igrac, stanje)

    moguci_potezi = nova_stanja(len(velika_tabla),igrac)

    if igrac == 'X': #to nam je MAX_IGRAC
        v = float('-inf')
        for i, j, poslednji, poRedu, prostor in moguci_potezi:
            v = max(v, minmax_alpha_beta(promeni_igraca(igrac), j, dubina - 1, alfa, beta))
            alfa = max(alfa, v)
            if beta <= alfa:
                break  # Odsecanje beta grane
        return v
    else:
        v = float('inf')
        for i, j, poslednji, poRedu, prostor in moguci_potezi:
            v = min(v, minmax_alpha_beta(promeni_igraca(igrac), j, dubina - 1, alfa, beta))
            beta = min(beta, v)
            if beta <= alfa:
                break  # Odsecanje alfa grane
        return v

# def min_value(stanje, dubina, alpha, beta):
#     lista_novih_stanja = nova_stanja(stanje)
#     if dubina == 0 or lista_novih_stanja is None:
#         return (stanje, proceni_stanje(stanje))
#     else:
#         for s in lista_novih_stanja:
#             beta = min(beta,
#                        max_value(s, dubina - 1, alpha, beta),
#                        key=lambda x: x[1])
#             if beta[1] <= alpha[1]:
#                 return alpha
#         return beta

# def max_value(stanje, dubina, alpha, beta):
#     lista_novih_stanja = nova_stanja(stanje)
#     if dubina == 0 or lista_novih_stanja is None:
#         return (stanje, proceni_stanje(stanje))
#     else:
#         for s in lista_novih_stanja:
#             alpha = max(alpha,
#                         min_value(s, dubina - 1, alpha, beta),
#                         key=lambda x: x[1])
#             if alpha[1] >= beta[1]:
#                 return beta
#         return alpha

# def minimax(stanje, dubina, moj_potez, alpha, beta):
#     if moj_potez:
#         return max_value(stanje, dubina, alpha, beta)
#     else:
#         return min_value(stanje, dubina, alpha, beta)

def kraj(tabla):
    n = len(tabla)
    ukupanBrojStekova = int((n - 2) * (n / 2) / 8)
    if (stekX > stekO and (stekX >= (ukupanBrojStekova + 1) // 2)):
        return 10 #vracam 10 kao je pobedio X
    elif (stekX < stekO and (stekO >= (ukupanBrojStekova // 2))):
        return -10 #vracam -10 ako je pobedio O
    count = [sum(1 for row in matrix for elem in row if elem != '.') for matrix in velika_tabla]
    total_count = sum(count)
    if (total_count == 0):
        return 0 #vracam 0 kao je nereseno

def najbolji_potez(igrac, stanje, dubina):
    moguci_potezi = nova_stanja(len(velika_tabla), igrac)
    najbolji_potez = None
    najbolja_vrednost = float('-inf') if igrac == 'X' else float('inf')

    for potez, lista_poteza in moguci_potezi.items():
        for pojedinacni_potez in lista_poteza:
            vrednost_poteza = minmax_alpha_beta(promeni_igraca(igrac), pojedinacni_potez, dubina - 1, float('-inf'), float('inf'))

            if (igrac == 'X' and vrednost_poteza > najbolja_vrednost) or (igrac == 'O' and vrednost_poteza < najbolja_vrednost):
                najbolja_vrednost = vrednost_poteza
                najbolji_potez = (potez, pojedinacni_potez)

    return najbolji_potez




def igraj_partiju():
    trenutni_igrac = 'X'
    stanje = pocetnoStanje()

    while not igra_je_zavrsena(velika_tabla):
        print("Trenutno je na potezu (" + trenutni_igrac + ")")
        print("Rezultat: (X)", stekX, ": (O)", stekO)
        if trenutni_igrac == 'X':
            potez = najbolji_potez(trenutni_igrac, stanje, dubina=3)
            print("Trenutno je na potezu (" + trenutni_igrac + ")")
            print("Rezultat: (X)", stekX, ": (O)", stekO)
            kljuc, lista_poteza = potez

            trenutniRed, trenutnaKol, vrh, poRedu, preostaloMesta = kljuc
            noviRed, novaKol,  mestaZaNove = lista_poteza
            #OVDE REMOVEEE
            niz = remove_figures_from_matrix(velika_tabla, trenutniRed, trenutnaKol, poRedu, 3, 3, trenutni_igrac, noviRed, novaKol)
            #E SAD IH PREBACIMO
            mala_matrica = velika_tabla[noviRed][novaKol]
            if (potez_validan(noviRed, novaKol, trenutniRed, trenutnaKol)):
                niz_izbacenih = niz
                k = 0
                napusti_petlje = False

                for i in range(3):
                    for j in range(3):
                        if mala_matrica[i][j] == '.':
                            mala_matrica[i][j] = niz_izbacenih[k]
                            k += 1

                            if k == len(niz_izbacenih):
                                #print(mala_matrica)
                                pr = provera_male_matrice(mala_matrica)

                                if pr == 8:
                                    poslednji = mala_matrica[2][1]
                                    pobedio(velicina_vece_table, poslednji)
                                    reset_mala(mala_matrica)

                                napusti_petlje = True
                                break  # Izlazimo iz unutrašnje for petlje

                    if napusti_petlje:
                        break

        else:
            # Implementiraj unos poteza od strane čoveka
            potez = unos_poteza(trenutni_igrac)
            while (potez == None):
                potez = unos_poteza(trenutni_igrac)


        ispisi_veliku_tablu(velika_tabla)

        trenutni_igrac = promeni_igraca(trenutni_igrac)
    rezultat = proceni_stanje('X', stanje, vrh) - proceni_stanje('O', stanje, vrh)
    if rezultat > 0:
        print("Pobedio je X!")
    elif rezultat < 0:
        print("Pobedio je O!")
    else:
        print("Nerešeno!")


if __name__ == "__main__":
    #
    stekX = 0
    stekO = 0
    #nacinIgranja = ()
    #nacinIgranja = podesavanje_igre() #vraca 2 za igru sa racunarom
    opcija, _ = podesavanje_igre() #vraca 2 za igru sa racunarom, opcija je to
    #print(opcija)


    print("Unesite dimenziju matrice: (8, 10 ili 16) ")
    velicina_vece_table = int(input())
    while (velicina_vece_table != 8 and velicina_vece_table != 10 and velicina_vece_table != 16):
        print("Nije validna dimenzija")
        velicina_vece_table = int(input("Unesite dimenziju matrice: (8, 10 ili 16) "))



    trenutni_igrac = 'X'
    velika_tabla = [
        [kreiraj_malu_tablu_t() if (row_index + col_index) % 2 == 0 else kreiraj_malu_tablu_b()
         for col_index in range(velicina_vece_table)]
        for row_index in range(velicina_vece_table)
    ]
    ikslg = []
    okslg = []
    mx = []
    my = []
    for x in range(2, velicina_vece_table, 2):
        for y in range(2, velicina_vece_table + 1, 2):
            ikslg.append([x, y])
    for x in range(3, velicina_vece_table, 2):
        for y in range(1, velicina_vece_table, 2):
            okslg.append([x, y])


    pocetnoStanje()
    ispisi_veliku_tablu(velika_tabla)
    #print(nova_stanja(velicina_vece_table, trenutni_igrac)) #INACE STOJI DOLE U WHILE


    o = 0
    b = 0

    #print(generisiSvaStanja(velicina_vece_table))
    if (opcija == 2):
        igraj_partiju()
    else:
        while True:

            if(o == 0):
                print("Trenutno je na potezu (" + trenutni_igrac+")")
                potez = unos_poteza(trenutni_igrac)
                # if(potez == "X"):
                #     continue

                if (potez == None):
                    potez = trenutni_igrac

                br = potez
                tr = potez
                o = o+1

                if potez !=None:

                    ispisi_veliku_tablu(velika_tabla)
                    print("Rezultat: (X)", stekX, ": (O)", stekO)
                    print("Trenutno je na potezu (" + tr+")")


                continue
            else:
                br = tr
                tr = unos_poteza(tr)

                if tr !=None:
                    ispisi_veliku_tablu(velika_tabla)
                    print("Rezultat: (X)", stekX, ": (O)", stekO)

                    print("Trenutno je na potezu (" + tr+")")

                if (tr == None):
                    tr = br






