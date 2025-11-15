import requests 
import json

def getpokemon_data(name):
    # creating api url
    api_url= f"https://pokeapi.co/api/v2/pokemon/{name}"
    # we'll take data from this api
    # this api will give us random data about hypothetical users

    # send request
    res=requests.get(api_url)

    try:
        if res.status_code==200:
            print(f"Status code is {res.status_code} and ready to use")

            # convert data itno json
            data = res.json()

            print("Pokemon Name : ", data['name'])
            print("Pokemon Specific ID: ", data['id'])
            print("Pokemon Height: ", data['height'])
            print("Pokemon Weight: ", data['weight'])

        else: 
            print("Failed to retrieve data from API ", res.status_code)
    
    except requests.exceptions.RequestException as e:
        print("API Error ", e)

pokemon_name=input("Enter your favorite pokemon name: ")
getpokemon_data(pokemon_name)
