import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

# Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

print(data[0]['id'])


def allpokes():
    lang = input("what langauge?")
    lang=lang.lower().replace(" ", "")
    if lang != "english" and lang != "french" and lang != "japanese" and lang != "chinese":
        print("language not included")
        return
    for id in enumerate(data):
        print(id[1]['name'][lang])
# allpokes()

def pokedexa():
    normaltypes = {
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice", 
    "Fighting", "Poison", "Ground", "Flying", "Psychic", 
    "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"
    }
    good=[]
    goodname=[]
    lang = input("what langauge?").lower().replace(" ", "")
    if lang != "english" and lang != "french" and lang != "japanese" and lang != "chinese":
        print("language not included")
        return
    tool = input("Search for type or name?").replace(" ", "")

    if tool == "type":
        type = input("what type?").replace(" ", "")
        if type not in normaltypes:
            print("not an existing type")
            return
        for id in enumerate(data):
            if type in id[1]['type']:
                good.append(id[1]['name'][lang])
        for poke in good:
            print(poke)

    elif tool == "name":
        names = input("what name?").replace(" ", "")
        for id in enumerate(data):
            if names in id[1]['names'][lang]:
                good.append(id[1]['name'][lang])
        for poke in goodname:
            print(poke)
        
pokedexa()