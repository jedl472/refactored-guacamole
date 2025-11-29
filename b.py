#!/usr/bin/env python3
import sys


def minimalni_cas(pocet_oken, okna):
    print(pocet_oken)

    okna_stripped = []                # stripnuti listu pocatecnich a koncovych znaku
    flag = False
    for i in okna:
        if i == 'X':
            flag = True
        if flag:
            okna_stripped.append(i)

    flag = False
    okna_stripped_reversed = reversed(okna_stripped)
    okna_stripped = []
    for i in okna_stripped_reversed:
        if i == 'X':
            flag = True
        if flag:
            okna_stripped.append(i)

    # print(okna_stripped)

    if len(okna_stripped) == 0:
        return 0

    space_len_pos = []
    current_len = 0
    current_start_pos = 0

    for i in enumerate(okna_stripped):               # nalezeni vsech sekvenci 'O'
        if i[1] == 'X':
            space_len_pos.append((current_len, current_start_pos + 1))
            current_start_pos = i[0]
            current_len = 0
        else:
            current_len += 1

    longest_len_pos = (0, 0)

    # print(space_len_pos)
 
    for i in space_len_pos:                          # nalezeni nejdelsi sekvence 'O'
        if i[0] > longest_len_pos[0]:
            longest_len_pos = i

    # print(longest_len_pos)

    okna_stripped_edited = []
    
    flag = False
    for i in enumerate(okna_stripped):               # sebrani nejdelsi sekvence 'O' a zjisteni vysledne delky seznamu
        if i[0] == longest_len_pos[1]:
            flag = True
        elif i[1] == 'X':
            flag = False
        if flag == False:
            okna_stripped_edited.append(i[1])
    
    # print(okna_stripped_edited)

    return len(okna_stripped_edited)


# Načítání vstupu


def precti_vstup(input, output):
    pocet_problemu = int(input.readline())

    for _ in range(pocet_problemu):
        pocet_oken = int(input.readline())
        okna = list(input.readline())
        if okna[-1] == '\n':
            okna = okna[:-1]

        reseni = minimalni_cas(pocet_oken, okna)

        output.write(f"{reseni}\n")


NAZVY_SOUBORU = [
    ("B-lehky.txt", "B-lehky-vystup.txt"),
    ("B-tezky.txt", "B-tezky-vystup.txt"),
]

soubor_nalezen = False

for nazev_vstupu, nazev_vystupu in NAZVY_SOUBORU:
    try:
        with open(nazev_vstupu, "r", 1, "utf-8") as vstup:
            with open(nazev_vystupu, "w", 1, "utf-8") as vystup:
                precti_vstup(vstup, vystup)

        soubor_nalezen = True

    except FileNotFoundError:
        pass

if not soubor_nalezen:
    precti_vstup(sys.stdin, sys.stdout)
