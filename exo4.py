from tkinter import *

fenetre = Tk()
fenetre.title("Seance de Cinema - Logiciel de gestion")
fenetre.geometry("400x300")

def click_btn(film_id, txt):
    print("click ok sur le film n°", film_id)
    print("Vous avez choisi le film:", films[film_id-1]['titre'])
    nb_places = films[film_id-1]['places']
    if nb_places > 0:
        print("Achat effectué !")
        films[film_id-1]['places'] -= 1
        txt.set(films[film_id-1]['places'])
        print("Le film possède désormais", films[film_id-1]['places'], "places !")
        print("_________________")
    else:
        print("Film complet !")
        print("_________________")
        txt.set("Film Complet !")
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
    places_var = StringVar()
    places_var.set(places)

    titre_label = Label(fenetre, text=titre)
    titre_label.grid(row=numero, column=0)

    seance_label = Label(fenetre, text=seance)
    seance_label.grid(row=numero, column=1)

    places_label = Label(fenetre, textvariable=places_var)
    places_label.grid(row=numero, column=2)

    book_bouton = Button(fenetre, text="Réserver", 
        command= lambda num = numero,
        txt = places_var: click_btn(num, txt))
    book_bouton.grid(row=numero, column=3)

fenetre.mainloop()