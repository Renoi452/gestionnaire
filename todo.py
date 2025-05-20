import json
import os

FICHIER_TACHES = "taches.json"

def charger_taches():
    if os.path.exists(FICHIER_TACHES):
        with open(FICHIER_TACHES, "r") as f:
            return json.load(f)
    return []

def sauvegarder_taches(taches):
    with open(FICHIER_TACHES, "w") as f:
        json.dump(taches, f, indent=2)

def ajouter_tache(description):
    taches = charger_taches()
    nouvelle_tache = {"description": description, "faite": False}
    taches.append(nouvelle_tache)
    sauvegarder_taches(taches)
    print(f"Tâche ajoutée : {description}")

def lister_taches():
    taches = charger_taches()
    if not taches:
        print("Aucune tâche dans la liste.")
        return
    print("\nListe des tâches :")
    for i, tache in enumerate(taches, start=1):
        statut = "✓" if tache["faite"] else "✗"
        print(f"{i}. [{statut}] {tache['description']}")

if __name__ == "__main__":
    while True:
        print("\nMenu :")
        print("1. Ajouter une tâche")
        print("2. Lister les tâches")
        print("3. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            desc = input("Description de la nouvelle tâche : ")
            ajouter_tache(desc)
        elif choix == "2":
            lister_taches()
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
