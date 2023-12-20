import requests
poke_name=input('Enter Pokemon name: ').lower()
base_url="https://pokeapi.co/api/v2/pokemon/"

url=f"{base_url}/{poke_name}"

response=requests.get(url)

if response.status_code==200:
    pokemon_data=response.json()
    # print(response.json())
    print("Pokemon Name: "f"{pokemon_data['name'].capitalize()}")
    print()
    
    print("Moves: ")
    for i in range(11):
        print(pokemon_data['moves'][i]['move']['name'])
        
    print()
    for i in range(len(pokemon_data['types'])):
        print("Type: "f"{pokemon_data['types'][i]['type']['name'].capitalize()}")
        
    else:
        print("Unable to retrieve information for ",poke_name,".")