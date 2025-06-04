import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '099c97c8a9cd35be056601c575af88c2'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}

body_pokemons = {
    "name": "Пипа",
    "photo_id": 1
}

body_new_name_pokemon = {
    "pokemon_id": "301978",
    "name": "Пупа"
}

body_pokemon_id= {
    "pokemon_id": "301978"
}


'''response_pokemon = requests.post(url=f'{URL}/pokemons',headers=HEADER,json=body_pokemons)
print (response_pokemon.text)''' 

'''response_pokemon_new_name = requests.patch(url=f'{URL}/pokemons',headers=HEADER,json=body_new_name_pokemon)
print (response_pokemon_new_name.text)'''

response_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json=body_pokemon_id)
print (response_pokeball.text)