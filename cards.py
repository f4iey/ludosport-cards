import os
import json
from jinja2 import Environment, FileSystemLoader

# Chargement des données depuis les fichiers JSON
fichiers = []
for nom_fichier in os.listdir("."):
    if nom_fichier.endswith(".json"):
        with open(nom_fichier) as f:
            data = json.load(f)
            fichiers.append(data)

# Configuration de Jinja pour charger le template HTML
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("index_template.html")

# Génération de la page HTML avec Jinja
page_html = template.render(fichiers=fichiers)

# Écriture de la page HTML dans un fichier
with open("index.html", "w") as f:
    f.write(page_html)
