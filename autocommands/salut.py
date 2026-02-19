import csv
import random

inconnu = []
connu = []
places = []
people = []
hellos = ["Hello, he was insulting me.", 
        "Hello, I'm Mr. Frog. This is my show. I eat the bug. (eats bug) I ate the bug. This is the end. I love you.",
        "Hello, but I\’m not sorry",
        "Hello I'm Mr. Frog and I approve this message. No I don't, I hate you f*ck you.",
        "Hello, i'm Mr. Frog, hello.",
        "Hello, I just watch Jimmy Fallon clips on YouTube all day.",
        "Hello. I know the world is very angry at me right now for my behavior. But I just wanted to say, from the bottom of my heart, that I'm sorry.",
         "HELLO I'M ROY DISMEY HELLO I'M ROY DISMEY THANK YOU FOR HAVING ME"]

def init():
    #on efface tout dans les listes, on importe chaques lignes des .csv et on les fous dans les listes
    inconnu.clear()
    connu.clear()
    places.clear()
    people.clear()
    with open('./data/csv/inconnu.csv', mode ='r', encoding='utf-8')as file:
        file = csv.reader(file)
        for line in file:
            inconnu.append(line[0].lower())
    with open('./data/csv/connu.csv', mode='r', encoding='utf-8') as file:
        file = csv.reader(file)
        for line in file:
            connu.append(line[0].lower())
    with open('./data/csv/places.csv', mode='r', encoding='utf-8') as file:
        file = csv.reader(file)
        for line in file:
            places.append(line[0].lower())
    with open('./data/csv/ids.csv', mode='r', encoding='utf-8') as file:
        file = csv.reader(file)
        for line in file:
            people.append(line[0].lower())

def sentence(slt):
    #une chance sur 6 de passer connu en 1er elem et 5 sur 6 de passer un inconnu et une place en 2e elem
    #de base, yavait aussi un truc qui avait 1 chance sur 6 de se déclencher et de mentionner les users, mais il est actuellement désactivé
    nb1 = random.randint(0, 6)
    nb3 = random.randint(0, len(places)-1)
    if nb1 == 0:
        nb2 = random.randint(0, len(connu)-1)
        return f"{slt}, c'est {connu[nb2]} {places[nb3]}!"
    #elif nb1 == 1:
        #nb2 = random.randint(0, len(people)-1) 
        #return f"{slt}, c'est <@{people[nb2]}> {places[nb3]}!"
    else:
        nb2 = random.randint(0, len(inconnu)-1) 
        return f"{slt}, c'est {inconnu[nb2]} {places[nb3]}!"

def hello():
    return hellos[random.randint(0, len(hellos)-1)]

