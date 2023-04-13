import json

# Demander le nom du fichier JSON à modifier
filename = input("Entrez le nom du fichier JSON à modifier : ")

# Vérifier si le fichier existe ou pas
try:
    with open(filename, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}

# Afficher le contenu actuel du fichier JSON
print("Contenu actuel :")
print(json.dumps(data, indent=4))

# Demander à l'utilisateur les modifications à apporter
while True:
    print("Que voulez-vous faire ?")
    print("1. Ajouter ou modifier une entrée")
    print("2. Supprimer une entrée")
    print("3. Quitter")

    choice = input("Entrez votre choix (1-3) : ")

    if choice == "1":
        key = input("Entrez le nom de la clé : ")
        value = input("Entrez la valeur de la clé : ")
        data[key] = value
    elif choice == "2":
        key = input("Entrez le nom de la clé à supprimer : ")
        if key in data:
            del data[key]
        else:
            print(f"La clé '{key}' n'existe pas dans le fichier.")
    elif choice == "3":
        break
    else:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

# Enregistrer les modifications dans le fichier JSON
with open(filename, "w") as f:
    json.dump(data, f, indent=4)

print("Modifications enregistrées dans le fichier.")
