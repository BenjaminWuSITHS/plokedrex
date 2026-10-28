import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
moves = open("./moves.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
move = json.load(moves)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

# Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

print(data[0]['id'])

def findmoves(namelist, type):
    if type == []:
        for id in data:
            for pokes in namelist:
                if pokes in id['name']['english']:
                    type.append(id["type"])
    for i, pokes in enumerate(namelist):
        print(f"{i}: {pokes}, {type[i]}")
    find = int(input("Which pokemon do you want to find the possible moves for? (The number)"))
    print(type[find])
    for i in range(len(type[find])):
        for types in move:
            if types['type'] == type[find][i]:
                print(types['ename'])


# findmoves(["Charizard", "Pikachu"], [])
findmoves(["Charizard", "Pikachu"], [["Fire", "Flying"], ["Electric"]])

def allpokes():
    lang = input("what langauge?")
    lang=lang.lower().replace(" ", "")
    if lang != "english" and lang != "french" and lang != "japanese" and lang != "chinese":
        print("language not included")
        return
    for id in data:
        print(id[1]['name'][lang])
# allpokes()

def pokedexa():
    normaltypes = {
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice", 
    "Fighting", "Poison", "Ground", "Flying", "Psychic", 
    "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"
    }
    languages = {
        "english", "french", "japanese", "chinese"
    }

    while True:
        print("Welcome to the pokedex!")
        go = input("Would you like to search for a pokemon?").lower().replace(" ", "")
        if go == 'yes':
            break
        elif go == 'no':
            return

    good=[]
    goodname=[]
    lang = input("Language?").lower().replace(" ", "")
    if lang not in languages:
        print("Language not included")
        return
    tool = input("Search for type or name?").replace(" ", "")

    if tool == "type":
        type = input("What type?").replace(" ", "")
        if type not in normaltypes:
            print("Not an existing type")
            return
        for id in data:
            if type in id[1]['type']:
                good.append(id[1]['name'][lang])
        for poke in good:
            print(poke)
        

    elif tool == "name":
        names = input("What name? Remember it is case-specific.").replace(" ", "")
        for id in data:
            if names in id[1]['name'][lang]:
                goodname.append(id[1]['name'][lang])
        if goodname == []:
            print("None found")
            return
        for poke in goodname:
            print(poke)
    tool2 = input("Search for moves?")
    if tool2.lower() == "yes":
        if tool == "name":
            findmoves(goodname,[])
        elif tool == "type":
            findmoves(good, [])
    else:
        return


#pokedexa()