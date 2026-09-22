from Fcts import lire_note, lire_texte, moyenne, modifier, rechercher, sauvegarde, supprimer, stagiaires, menu

def main():
    choix = 1
    while choix != 6:
        menu()
        try:
            choix = int(input("Donner votre choix : "))
        except ValueError:
            print("Veuillez choisir une option entre 1 et 6.")
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
        elif choix == 4:
            nom = lire_texte("Nom du stagiaire à supprimer :")
            try:
                supprimer(nom)
            except KeyError:
                print("Stagiaire non trouvé")
            else:
                print("Le stagiaire a été supprimé.")
        elif choix == 5:
            nom = lire_texte("Nom du stagiaire à modifier :")
            if nom not in stagiaires:
                print("Stagiaire non trouvé")
                continue
            prenom = lire_texte("Nouveau prénom :")
            notes = [
                lire_note("Nouvelle note 1ère année :"),
                lire_note("Nouvelle note communication :"),
                lire_note("Nouvelle note théorique :"),
                lire_note("Nouvelle note pratique :"),
            ]
            modifier(nom, prenom, notes)
            print("Le stagiaire a été modifié.")
        elif choix != 6:
            print("Veuillez choisir une option entre 1 et 6.")

    sauvegarde()

if __name__ == "__main__":
    main()
