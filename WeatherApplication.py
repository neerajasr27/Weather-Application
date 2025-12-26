import requests

city = input("Enter city name: ").strip()

url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    current = data["current_condition"][0]

    temperature = current["temp_C"]
    condition = current["weatherDesc"][0]["value"]

    print("\nWeather Details")
    print("----------------")
    print(f"City        : {city}")
    print(f"Temperature : {temperature} °C")
    print(f"Condition   : {condition}")
else:
    print("Unable to fetch weather data")
