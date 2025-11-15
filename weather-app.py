import requests
import json

# API key
api_key='8f554542bd68933d8c57355a0edbd308'

# city name input
city_name=input("Enter your city name to check the weather status: ")

# API URL
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

try: 
    res=requests.get(url)
    data=res.json()

    if res.status_code==200:
        print("API connection successful!")
        print(f"CITY NAME : {data['name']}  | VISIBILITY : {data['visibility']} |  TIME-ZONE : {data['timezone']}")
        print(f"TEMPERATURE : {data['main']['temp']} | HUMIDITY: {data['main']['humidity']} | WIND SPEED: {data['wind']['speed']}")

        # printing complete data
        p_data=json.dumps(data,indent=4)
        print(f"{city_name}'s overall data is : ")
        print(p_data)

except requests.exceptions.RequestException as e:
    print("API Error ", e)