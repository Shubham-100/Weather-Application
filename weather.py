import requests
import json
import tkinter as tk
from decimal import Decimal

api_key = "077d7c1218a047744015b2becc02b548"
base_url = "https://api.openweathermap.org/data/2.5/weather?appid="


def get_weather():
    city_name = input_label.get()
    link = base_url + api_key + "&q=" + city_name

    # Create an HTTP request message to OpenWeatherMap API
    response = requests.get(link)
    forecast = response.json()

    # Invalid city name and display appropriate error message
    if forecast["cod"] == "404":
        err = tk.Label(root, text="City not found, did you misspelled?")
        err.pack()
    elif forecast["cod"] == "400":
        err = tk.Label(root, text="Please enter the city...")
        err.pack()
    else:
        # Else clear the frame to display the weather details
        for widget in root.winfo_children():
            widget.destroy()

        temp = int(forecast["main"]["temp"]) - 273.15
        temp = round(Decimal(temp), 2)

        conditions = forecast["weather"]
        conditions = conditions[0]["description"]

        humidity = forecast["main"]["humidity"]
        wind = forecast["wind"]["speed"]
        wind_dir = forecast["wind"]["deg"]

        tmp = tk.Label(root, text=f'Temperature: {temp}{chr(176)}C')
        cdt = tk.Label(root, text=f'Conditions: {conditions}')
        hmdt = tk.Label(root, text=f'Humidity: {humidity}%')
        wnd = tk.Label(root, text=f'Winds: {wind} km/h, directing at {wind_dir}{chr(176)}')

        root.geometry("250x100")

        tmp.pack()
        cdt.pack()
        hmdt.pack()
        wnd.pack()


root = tk.Tk()
root.title("Weather Application")
root.geometry("250x80")

city = tk.Label(root, text="Enter your city here...")
city.focus_set()
city.pack()

# Input text field
input_label = tk.Entry(root)
input_label.pack()

search = tk.Button(root, text="Get Weather", command=get_weather)
search.pack()

root.mainloop()
