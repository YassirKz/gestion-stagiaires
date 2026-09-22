import json

# Chargement des données depuis data.json (ou dictionnaire vide si fichier absent)
try:
    with open("data.json", "r", encoding="utf-8") as file:
        stagiaires = json.load(file)
except Exception:
    stagiaires = {}

def menu():
    print("--------------------Menu----------------------")
    print("Press 1 to add a trainee")
    print("Press 2 to display the list of trainees")
    print("Press 3 to search for a trainee")
    print("Press 4 to exit")
    print("----------------------------------------------")

def rechercher(nom):
    """Retourne le dictionnaire du stagiaire identifié par `nom`.

    Lève KeyError si le nom n'existe pas.
    """
    return stagiaires[nom]

def moyenne(notes):
    """Calcule la moyenne d'une liste de notes (strings ou nombres)."""
    if not notes:
        return 0
    total = 0.0
    for n in notes:
        total += float(n)
    return total / len(notes)

def sauvegarde():
    """Sauvegarde le dictionnaire `stagiaires` dans `data.json`."""
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(stagiaires, file, indent=4, ensure_ascii=False)
