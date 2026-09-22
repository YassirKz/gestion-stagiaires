import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("data.json")

def charger_donnees():
    """Charge les stagiaires sans remplacer silencieusement un fichier invalide."""
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            donnees = json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise RuntimeError("Le fichier data.json est corrompu.") from exc

    if not isinstance(donnees, dict):
        raise RuntimeError("Le fichier data.json doit contenir un objet JSON.")
    return donnees

stagiaires = charger_donnees()

def menu():
    print("--------------------Menu----------------------")
    print("Press 1 to add a trainee")
    print("Press 2 to display the list of trainees")
    print("Press 3 to search for a trainee")
    print("Press 4 to exit")
    print("----------------------------------------------")

def lire_note(libelle):
    """Demande une note valide comprise entre 0 et 20."""
    while True:
        try:
            note = float(input(libelle))
            if 0 <= note <= 20:
                return note
        except ValueError:
            pass
        print("Veuillez saisir une note comprise entre 0 et 20.")

def lire_texte(libelle):
    """Demande un texte non vide."""
    while True:
        valeur = input(libelle).strip()
        if valeur:
            return valeur
        print("Ce champ ne peut pas être vide.")

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
    """Sauvegarde les données dans data.json."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(stagiaires, file, indent=4, ensure_ascii=False)
