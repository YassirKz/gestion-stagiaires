from getpass import getpass
from pathlib import Path

ACCOUNT_FILE = Path(__file__).with_name("comptes.pas")

def verifier(login, password):
    """Retourne True si le login et le mot de passe sont corrects."""
    try:
        lines = ACCOUNT_FILE.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        print("Le fichier comptes.pas est absent.")
        return False

    for line in lines:
        parts = line.split(";")
        if len(parts) < 2:
            continue
        if parts[0].strip() == login and parts[1].strip() == password:
            return True
    return False

def main():
    for _ in range(3):
        login = input("Login : ").strip()
        password = getpass("Password : ")
        if verifier(login, password):
            print("Bienvenue !")
            return 0
        print("Login ou mot de passe incorrect.")

    print("Accès refusé après trois tentatives.")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())

