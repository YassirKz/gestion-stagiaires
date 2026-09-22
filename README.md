# 🎓 Gestion des Stagiaires

Application Python de gestion de stagiaires avec authentification.

## ✨ Fonctionnalités

- 🔐 Authentification (login / mot de passe)
- ➕ Ajouter un stagiaire
- 📋 Afficher la liste des stagiaires
- 🔍 Rechercher un stagiaire + calcul de moyenne
- 🗑️ Supprimer un stagiaire
- ✏️ Modifier un stagiaire
- 💾 Sauvegarde automatique dans `data.json`

## 📂 Structure

| Fichier                | Description                                         |
| ---------------------- | --------------------------------------------------- |
| `comptes.pas.example`  | Modèle des identifiants (à copier en `comptes.pas`) |
| `data.json`            | Base de données des stagiaires                      |
| `Fcts.py`              | Fonctions utilitaires                               |
| `password.py`          | Module d'authentification                           |
| `Student_managment.py` | Programme principal                                 |

## 🚀 Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/YassirKz/gestion-stagiaires.git
cd gestion-stagiaires
```

2. Créer le fichier d'identifiants à partir de l'exemple :

```bash
cp comptes.pas.example comptes.pas
```

3. Modifier `comptes.pas` avec vos identifiants.
4. Lancer :

```bash
python password.py
python Student_managment.py
```

> ⚠️ `comptes.pas` n'est pas versionné (sécurité).
>
> Le fichier `comptes.pas.example` contient uniquement des valeurs de démonstration.

## 🛠️ Technologies

- Python 3.x
- JSON (persistance des données)

## 👤 Auteur

[@YassirKz](https://github.com/YassirKz)
