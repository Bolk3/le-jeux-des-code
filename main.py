from random import *
import sys

def selection_difficulte():
    r = []
    bon_choix = 1
    while bon_choix == 1:
        choix = input("veuillez choisir une option ci-dessous\n1-FACILE (20 tentatives,code a 3 chiffres,nombre d'aide 5)\n2-DIFFICILE (10 tentative,code a 4 chiffres,nombre d'aide 2)\n3-PERSONALISEE\n")
        bon_choix = 1
        if choix == str(1):
            r.append(20)
            r.append(3)
            r.append(5)
            bon_choix = 0
        elif choix == str(2):
            r.append(10)
            r.append(4)
            r.append(5)
            bon_choix = 0
        elif choix == str(3):
            r.append(int(input("choissisez le nombres de tentatives:")))
            r.append(int(input("choissisez la taille du code:")))
            r.append(int(input("choissisez le nombre d'aide:")))
            bon_choix = 0
        else :
            print("vous n'avez pas choissis de bon arguments,retentez\n")
    print("la difficultée a ete selectionee\n\ntentative :", r[0], "\nlonguer du code:", r[1],"\n")
    return r

def generation_code(difficulty):
    r = []
    temp = []
    temp_ = ""
    for i in range(difficulty[1]):
        temp.append(randint(0,9))
    for i in range(len(temp)):
        temp_ = temp_ + str(temp[i])
    r.append(int(temp_))
    r.append(temp)
    return r

def indice_logique(difficulty, code_gagnant):
    x = []
    aide =[]
    for i in range(difficulty[2]):
        r =[]
        bon_nombre = 0
        temp = generation_code(difficulty)
        for k in range(len(temp)):
            if temp[1][k] == code_gagnant[1][k]:
                bon_nombre += 1
        r.append(temp)
        r.append(bon_nombre)
        aide.append(r)
    for i in range(len(aide)):
        x.append(["code :", aide[i][0], "nombre de nombre juste :", aide[i][1]])
    return x

def tour (difficulty, code, hint):
    tentative =[]
    essaie = 0
    i = 0
    bonne_reponse = 0
    while bonne_reponse == 0:
        if i < difficulty[0] :
            if i == 0:
                for i in range(len(hint)):
                    print(hint[i])
                essaie = input("\nquel est le code ? ")
            else :
                for i in range(len(hint)):
                    print(hint[i])
                print("les tentatives sont: ", tentative)
                essaie = input("\nquel est le code ? ",)

            tentative.append(essaie)
            if essaie != str(code[0]):
                print("ce n'est pas le code")
                i = len(tentative)
                bonne_reponse = 0
            elif essaie == str(code[0]):
                print("\nle code etait bien:", code[0], "\nfelicitation vous avez reussit en ", len(tentative),"tentative")
                bonne_reponse = 1
        else :
            print("\nvous n'avez pas reussit a trouvez le code en ", difficulty[0],"essais\nle code etait ",code[0])
            bonne_reponse = 1

def main():
    choix = ""
    print("/////////////////////////////////////////")
    print("//                                     //")
    print("//          LE JEUX DU CODE            //")
    print("//                                     //")
    print("/////////////////////////////////////////")
    choix = input("\n1-JOUER\n2-REGLES\n3-QUITER\n")
    izi = 0
    while izi == 0:
        if choix == str(1):
            jouer = 1
            choix_logic = 0
            while jouer == 1:
                d = selection_difficulte()
                c = generation_code(d)
                h = indice_logique(d, c)
                tour(d, c, h)
                while choix_logic == 0:
                    test_game = input("\nvoulez refaire une partie\n1-OUI\n2-NON\n")
                    if test_game == str(1):
                        jouer = 1
                        choix_logic = 1
                    elif test_game == str(2):
                        print("c'est triste que vous nous quittier")
                        sys.exit()
                    else:
                        print("c'est pas complique d'ecrir 1 ou 2 bon sang de bonsoir")
        elif choix == str(2):
            print("\n//---LES REGLES---//")
            print("le jeux consiste a trouver le code choisis aleatoirement \n")
            choix = input("\n1-JOUER\n2-REGLES\n3-QUITER\n")
        elif choix == str(3):
            print("c'est triste que vous nous quittier")
            sys.exit()
        else :
            print("c'est pas complique d'ecrir 1, 2 ou 3 bon sang de bonsoir")

main()