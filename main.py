import tkinter as tk
import requests
from PIL Wimport ImageTk, Image

#the function to fetch weather data
def get_weather():
    city = city_entry.get()
    # Unique public OpenWeatherMap API key from: https://openweathermap.org/api
    api_key = "f0e8bd26be4ad8375fac4cda3de15cbf"
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(api_url)
    weather_data = response.json()

    if response.status_code == 200:
        condition = weather_data['weather'][0]['main']
        temp = weather_data['main']['temp']
        min_temp = weather_data['main']['temp_min']
        max_temp = weather_data['main']['temp_max']
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        #Here we update the labels with weather information
        condition_label.config(text=condition)
        temperature_label.config(text=f"{int(temp)}°C")
        min_temp_label.config(text=f"Min Temp: {int(min_temp)}°C")
        max_temp_label.config(text=f"Max Temp: {int(max_temp)}°C")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")

        status_label.config(text="Weather information updated successfully!")
    else:
        status_label.config(text="Failed to retrieve weather information.")

#creatinng the main window
window = tk.Tk()
window.title("Weather App")

#configure window dimensions
window_width = 600
window_height = 500
window.geometry(f"{window_width}x{window_height}")
window.resizable(False, False)

#creatinng the background image
#backgroound image source: https://wallsheaven.co.uk/photos/pastel-weather
background_image = Image.open("background.jpg")
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#creatinng input frame
input_frame = tk.Frame(window, bg="white", bd=5)
input_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

#creatinng city entry field
city_entry = tk.Entry(input_frame, font=("Arial", 14))
city_entry.place(relwidth=0.65, relheight=1)

#making search button
search_button = tk.Button(input_frame, text="Search", font=("Arial", 12, "bold"), bg="#e6e6e6",
                          activebackground="#cccccc", command=get_weather)
search_button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

#making the weather info frame
weather_info_frame = tk.Frame(window, bg="white", bd=5)
weather_info_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.5, anchor="n")

#create labels to display weather information
condition_label = tk.Label(weather_info_frame, text="", font=("Arial", 24, "bold"), bg="white")
condition_label.pack()

temperature_label = tk.Label(weather_info_frame, text="", font=("Arial", 40, "bold"), bg="white")
temperature_label.pack()

min_temp_label = tk.Label(weather_info_frame, text="", font=("Arial", 14), bg="white")
min_temp_label.pack()

max_temp_label = tk.Label(weather_info_frame, text="", font=("Arial", 14), bg="white")
max_temp_label.pack()

pressure_label = tk.Label(weather_info_frame, text="", font=("Arial", 14), bg="white")
pressure_label.pack()

humidity_label = tk.Label(weather_info_frame, text="", font=("Arial", 14), bg="white")
humidity_label.pack()

wind_speed_label = tk.Label(weather_info_frame, text="", font=("Arial", 14), bg="white")
wind_speed_label.pack()

#creatinng status label
status_label = tk.Label(window, text="", font=("Arial", 12), bg="white")
status_label.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.1, anchor="n")

# run the application
window.mainloop()
