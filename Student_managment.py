from Fcts import lire_note, lire_texte, moyenne, rechercher, sauvegarde, stagiaires, menu

def main():
    choix = 1
    while choix != 4:
        menu()
        try:
            choix = int(input("Donner votre choix : "))
        except ValueError:
            print("Veuillez choisir une option entre 1 et 4.")
            continue

        if choix == 1:
            nom = lire_texte("Nom :")
            if nom in stagiaires:
                print("Un stagiaire avec ce nom existe déjà.")
                continue
            prenom = lire_texte("Prénom :")
            notes = [
                lire_note("Note 1ère année :"),
                lire_note("Note communication :"),
                lire_note("Note théorique :"),
                lire_note("Note pratique :"),
            ]
            stagiaires[nom] = {'prenom': prenom, 'notes': notes}
            print("Le stagiaire est bien enregistré")
        elif choix == 2:
            print("-------------------- Liste des stagiaires ---------------")
            for nom, stagiaire in stagiaires.items():
                print("Nom:", nom, " | Prénom:", stagiaire["prenom"], "| Notes:", ", ".join(map(str, stagiaire["notes"])))
            print("---------------------------------------------------------")
        elif choix == 3:
            nom = lire_texte("Donner le nom recherché :")
            try:
                stagiaire = rechercher(nom)
            except KeyError:
                print("Stagiaire non trouvé")
                continue
            print("----------------- Informations du stagiaire", nom, "----------------")
            print("Nom:", nom)
            print("Prénom:", stagiaire["prenom"])
            print("Moyenne:", moyenne(stagiaire["notes"]))
            print("---------------------------------------------------------")
        elif choix != 4:
            print("Veuillez choisir une option entre 1 et 4.")

    sauvegarde()

if __name__ == "__main__":
    main()
