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
        "places": 1
    }
]

for numero, film in enumerate(films, start=1):
    titre = film['titre']
    seance = film['seance']
    places = film['places']

    print(f"Film n°{numero} : {titre} : {seance} : ({places}) places dispo")

while True:
    print ("Inscrivez le numero du film à voir (1, 2 ou 3)")
    choix = int(input())
    print("Vous avez choisi le film:", films[choix-1]['titre'])
    nb_places = films[choix-1]['places']
    if nb_places > 0:
        print("Achat effectué !")
        films[choix-1]['places'] -= 1
        print("Le film possède désormais", films[choix-1]['places'], "places !")
        print("_________________")
    else:
        print("Film complet !")
        print("_________________")