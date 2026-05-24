rejouer='yes'
while True:
    DESSINS_PENDU = [
"""
  +-------+
  |
  |
  |
  |
  |
==============
""",
"""
  +-------+
  |       |
  |       O
  |
  |
  |
==============
""",
"""
  +-------+
  |       |
  |       O
  |       |
  |
  |
==============
""",
"""
  +-------+
  |       |
  |       O
  |      -|
  |
  |
==============
""",
"""
  +-------+
  |       |
  |       O
  |      -|-
  |
  |
==============
""",
"""
  +-------+
  |       |
  |       O
  |      -|-
  |      |
  |
==============
""",
"""
  +-------+
  |       |
  |       O
  |      -|-
  |      | |
  |
==============
"""
]
    from random import choice
    lst=["integral","derivative","limits","couscous","carrot","pickle","flower","house","pebble"]
    mot_mystère=choice(lst)
    lst_mot=[]
    for i in range(len(mot_mystère)):
        lst_mot.append(mot_mystère[i])
    longueur_mot=len(mot_mystère)
    lst_mystère=[]
    for SHAW in range(longueur_mot):
        lst_mystère.append("_")
    fautes=0
    lettres_complete=0
    lettre_utilisee=[]
    if rejouer!="yes":
        print("End of program")
        break
    while True:
        print(lst_mystère)
        stopping=0
        nop=0
        choix_lettre=input("Choose a letter: ")
        for EDINO in range(len(lettre_utilisee)):
                    if choix_lettre==lettre_utilisee[EDINO]:
                        nop+=1
        if nop!=0:
            print("This letter has already been used!")
            pass
        else:
            for j in range(len(mot_mystère)):
                if choix_lettre==mot_mystère[j]:
                    lst_mystère[j]=choix_lettre
                    print("Well done! Here is the word: ")
                    stopping+=1
                    lettres_complete+=1
                lettre_utilisee.append(choix_lettre)
            if stopping==0:
                if fautes>5:
                    print(DESSINS_PENDU[fautes])
                    print("You lost! The word was:", mot_mystère)
                    rejouer=input("Do you want to play again? ")
                    break
                print("Too bad! This letter is not in the word")
                print(DESSINS_PENDU[fautes])
                fautes+=1
            if lettres_complete==len(mot_mystère):
                print("Congratulations! You won! The word was indeed", mot_mystère)
                rejouer=input("Do you want to play again? ")
                break