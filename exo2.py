# afficher un message de bienvenue 
print("Bienvenue au cinema, voici les films à l'affiche: ")

films = [
    { # film 1
        "titre": "Voyage au centre du HTML",
        "seance": "18h05",
        "places": 200
    },
    { # film 2
        "titre": "Les 9 jsons cachés",
        "seance": "10h10",
        "places": 80
    }, 
    { # film 3
        "titre": "Algobox - le film",
        "seance": "22h15",
        "places": 120
    }
]

for numero, film in enumerate(films, start=1):
    titre = film['titre']
    seance = film['seance']
    places = film['places']

    print(f"Film n°{numero} : {titre} : {seance} : ({places}) places dispo")