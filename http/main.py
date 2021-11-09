import requests
from pokemon import Pokedex

i = 1
while(i < 5):
    request = requests.get("https://pokeapi.co/api/v2/pokemon/%s" % i)
    pokemon = Pokedex.from_dict(request.json())
    print(pokemon.name)
    i+=1

#pokemon = pokedex_from_dict(request.text)