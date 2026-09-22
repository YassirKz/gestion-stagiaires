choix=1

from Fcts import *

while choix !=4 :
    menu()
    choix=int(input("Donner votre choix : "))
    if choix==1 :
        nom=input("Nom :")
        prenom = input("Prénom :")
        note1 = input("Note 1ére année :")
        note2 = input("Note communication :")
        note3 = input("Note Théorique :")
        note4 = input("Note Pratique :")
        stagiaires[nom]={'prenom':prenom,'notes':[note1,note2,note3,note4]}
        print("Le stagiare est bien enregistré")
    if choix==2 :
        print("-------------------- Liste des stagiaires ---------------")
        for st in stagiaires.items() :
            print("Nom:",st[0]," | Prénom:",stagiaires[st[0]]["prenom"],"| Note1éreAnnée:",stagiaires[st[0]]["notes"][0],"| NoteCommunication:",stagiaires[st[0]]["notes"][1],"| NoteTH:",stagiaires[st[0]]["notes"][2],"| NotePR:",stagiaires[st[0]]["notes"][3])
        print("---------------------------------------------------------")
    if choix==3 :
        try:
            nom=input("donner le nom recherché:")
            st=rechercher(nom)
            print("----------------- Informations du stagiaire",nom,"----------------")
            print("Nom:",nom)
            print("Prénom:",st["prenom"])
            T_notes=st["notes"]
            print("Moyenne:",moyenne(T_notes) )
            print("---------------------------------------------------------")
        except:
            print("Stagiaire non trouvé")

else:
    sauvegarde()
