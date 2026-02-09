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
        "Hello. I know the world is very angry at me right now for my behavior. But I just wanted to say, from the bottom of my heart, that I'm sorry."]

def init():
    with open('./data/csv/inconnu.csv', mode ='r', encoding='utf-8')as file:
        file = csv.reader(file)
        for line in file:
            inconnu.append(line[0])
    with open('./data/csv/connu.csv', mode='r', encoding='utf-8') as file:
        file = csv.reader(file)
        for line in file:
            connu.append(line[0])
    with open('./data/csv/places.csv', mode='r', encoding='utf-8') as file:
        file = csv.reader(file)
        for line in file:
            places.append(line[0])
    with open('./data/csv/ids.csv', mode='r', encoding='utf-8') as file:
        file = csv.reader(file)
        for line in file:
            people.append(line[0])

def sentence(slt):
    nb1 = random.randint(0, 6)
    nb3 = random.randint(0, len(places)-1)
    if nb1 == 0:
        nb2 = random.randint(0, len(connu)-1)
        return f"{slt}, c'est {connu[nb2]} {places[nb3]}!"
    elif nb1 == 1:
        nb2 = random.randint(0, len(people)-1) 
        return f"{slt}, c'est <@{people[nb2]}> {places[nb3]}!"
    else:
        nb2 = random.randint(0, len(inconnu)-1) 
        return f"{slt}, c'est {inconnu[nb2]} {places[nb3]}!"

def hello():
    return hellos[random.randint(0, len(hellos)-1)]
