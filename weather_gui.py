from tkinter import *
from weather_api_config import api_config, temperature, climate

app_height = 500
app_width = 500
window_width = 400
window_height = 400


def weather_gui():
    global app_height, app_width, window_height, window_width

    # Creation of the GUI using Tkinter, config settings for the overall canvas.

    window = Tk()
    window.title = "Weather GUI"
    weather_app_gui = Canvas(window, height=app_height, width=app_width)
    weather_app_gui.pack()

    # Incorporated Label with functionality name of GUI

    label = Label(weather_app_gui, text="Weather App",
                  font=("Helvetica", 40), fg='#acd9e9')
    label.pack()

    # Canvas where Application functions will be represented, functions etc

    canvas = Canvas(window, bg='#acd9e2', height=window_height, width=window_width)
    canvas.pack()

    # Entry Box Configuration for Input/Output Functions

    input_box = Entry(window)
    input_box.place(x=110, y=250)

    input_entry_label = Label(window, font=("Helvetica", 20), width=20, height=2)
    input_entry_label.place(x=85, y=170)

    def get_weather():
        user_input = input_box.get()
        weather_data = api_config(input_box.get())

        if weather_data:
            input_entry_label.config(text=user_input.title())
            climate_label = Label(window, font=("Helvetica", 10), width=10, height=2, text=climate(user_input))
            climate_label.place(x=10, y=100)

            temperature_label = Label(window, font=("Helvetica", 10), width=10, height=2, text=temperature(user_input))
            temperature_label.place(x=10, y=300)
        else:
            input_entry_label.config(text="No data found")



    btn = Button(window, text='Enter', command=get_weather)
    btn.place(x=170, y=300)

    # Initiates the window to be created.

    window.bind("<Return>", lambda event:get_weather())
    weather_app_gui.mainloop()


weather_gui()