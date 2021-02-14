from tkinter import *
import pandas
from matplotlib import pyplot
from PIL import ImageTk, Image

###------------------------------------------BACKGROUND----------------------------------------------------##
WHITE = "#ffffff"
BUTTON_BG = "#c5f4e0"
WINDOW_BG = "#aceca1"
DARK_BLUE = "#23689b"
JET = "#1a1627"
PEACH = "#FFE5B4"
BLACK = "#17252A"
# ------------------------------------------FUNCTIONALITY----------------------------------------------------#
energy_data = pandas.read_csv("Resources.csv")
renewable_data = pandas.read_csv("renewable.csv")

colors = ["#DD614A", "#F48668", "#F4A698", "#C5C392", "#73A580", "#7E2E84", "#CCF5AC", "#363537", "#8CD867", "#2FBF71",
          "#FF6B35", "#F8F32B", "#C9F299", "#9CBFA7", "#20A4F3", "#59F8E8", "#BDC667", "#FF5964", "#FFFFFF", "#48BF84",
          "#000000", "#326273", "#A30015", "#C89FA3", "#16DB93", "#004F2D", "#8367C7", "#519872"]


def hydro():
    hydro_data = {row['STATES']: row['HYDRO'] for index, row in energy_data.iterrows() if row['HYDRO'] != 0}
    pyplot.pie([value for value in hydro_data.values()], autopct='%1.0f%%', radius=1.2, colors=colors, pctdistance=1.1)
    pyplot.legend(labels=[key for key in hydro_data.keys()], loc="upper left", ncol=3, bbox_to_anchor=(-0.9, 1))
    pyplot.title("HYDRO (in MW)", color="red", loc="right")
    pyplot.show()


def nuclear():
    nuclear_data = {row['STATES']: row['NUCLEAR'] for index, row in energy_data.iterrows() if row['NUCLEAR'] != 0}
    pyplot.pie([value for value in nuclear_data.values()], autopct='%1.0f%%', radius=1.2, colors=colors,
               pctdistance=1.1)
    pyplot.legend(labels=[key for key in nuclear_data.keys()], loc="upper left", ncol=3, bbox_to_anchor=(-0.9, 1))
    pyplot.title("NUCLEAR (in MW)", color="red", loc="right")
    pyplot.show()


def thermal():
    thermal_data = {row['STATES']: row['THERMAL'] for index, row in energy_data.iterrows() if row['THERMAL'] != 0}
    pyplot.pie([value for value in thermal_data.values()], autopct='%1.0f%%', radius=1.2, colors=colors,
               pctdistance=1.1)
    pyplot.legend(labels=[key for key in thermal_data.keys()], loc="upper left", ncol=3, bbox_to_anchor=(-0.9, 1))
    pyplot.title("THERMAL (in MW)", color="red", loc="right")
    pyplot.show()


def wind_power():
    wind_data = {row['States']: row['Wind Power'] for index, row in renewable_data.iterrows() if row['Wind Power'] != 0}
    pyplot.pie([value for value in wind_data.values()], colors=colors, autopct='%1.0f%%', radius=1.2, pctdistance=1.1)
    pyplot.legend(labels=[s for s in wind_data.keys()], loc="upper left", ncol=3, bbox_to_anchor=(-0.9, 1))
    pyplot.title("Wind Energy (in MW)", color="red", loc="right")
    pyplot.show()


def biomass():
    biomass_data = {row['States']: row['Biomass'] for index, row in renewable_data.iterrows() if row['Biomass'] != 0}
    pyplot.pie([value for value in biomass_data.values()], colors=colors, autopct='%1.0f%%', radius=1.2,
               pctdistance=1.06)
    pyplot.legend(labels=[s for s in biomass_data.keys()], loc="upper left", ncol=3, bbox_to_anchor=(-0.9, 1))
    pyplot.title("Biomass Energy (in MW)", color="red", loc="right")
    pyplot.show()


def solar_energy():
    solar_data = {row['States']: row['Solar Energy'] for index, row in renewable_data.iterrows() if
                  row['Solar Energy'] != 0}
    pyplot.pie([value for value in solar_data.values()], colors=colors, autopct='%1.0f%%', radius=1.2, pctdistance=1.1)
    pyplot.legend(labels=[s for s in solar_data.keys()], loc="upper left", ncol=3, bbox_to_anchor=(-0.9, 1))
    pyplot.title("Solar Energy (in MW)",color="red",loc="right")
    pyplot.show()


def waste_to_energy():
    waste_energy_data = {row['States']: row['Waste to Energy'] for index, row in renewable_data.iterrows() if
                         row['Waste to Energy'] != 0}
    pyplot.pie([value for value in waste_energy_data.values()], colors=colors, autopct='%1.0f%%', radius=1.2,
               pctdistance=1.1)
    pyplot.legend(labels=[s for s in waste_energy_data.keys()], loc="upper left", ncol=3, bbox_to_anchor=(-0.9, 1))
    pyplot.title("Waste to Energy (in MW)", color="red", loc="right")
    pyplot.show()


###------------------------------------------UI SETUP----------------------------------------------------###
def Energy_capacity():
    energy_window = Toplevel()
    energy_window.title("Foretree")
    energy_window.config(bg=WINDOW_BG, padx=50, pady=50)
    heading = Label(energy_window, text="Energy Capacity", bg=WINDOW_BG, font=("serif", 20, "bold"))
    heading.grid(row=0, column=0, columnspan=3)

    hydro_pic = Image.open("hydro.png")
    hydro_resized = hydro_pic.resize((80, 30), Image.ANTIALIAS)
    hydro_main = ImageTk.PhotoImage(hydro_resized)
    background = PhotoImage(file="foretree.png")
    canvas = Canvas(energy_window, width=322, height=326, bg=WINDOW_BG, highlightthickness=0)
    canvas.create_image(161, 163, image=background)
    canvas.grid(column=1, row=1, padx=20, pady=20)
    hydro_button = Button(energy_window, text="Hydro", image=hydro_main, highlightthickness=0, command=hydro,relief=FLAT)
    hydro_button.grid(row=2, column=0)
    hydro_label = Label(energy_window, text="Hydro", bg=WINDOW_BG)
    hydro_label.grid(row=3, column=0)
    thermal_pic = Image.open("thermal.png")
    thermal_resized = thermal_pic.resize((80, 30), Image.ANTIALIAS)
    thermal_main = ImageTk.PhotoImage(thermal_resized)
    thermal_button = Button(energy_window, image=thermal_main, highlightthickness=0, command=thermal,relief=FLAT)
    thermal_button.grid(row=3, column=1)
    thermal_label = Label(energy_window, text="Thermal", bg=WINDOW_BG)
    thermal_label.grid(row=4, column=1)
    nuclear_pic = Image.open("nuclear.png")
    nuclear_resized = nuclear_pic.resize((80, 30), Image.ANTIALIAS)
    nuclear_main = ImageTk.PhotoImage(nuclear_resized)
    nuclear_button = Button(energy_window, image=nuclear_main, highlightthickness=0, command=nuclear,relief=FLAT)
    nuclear_button.grid(row=2, column=2)
    nuclear_label = Label(energy_window, text="Nuclear", bg=WINDOW_BG)
    nuclear_label.grid(row=3, column=2)
    energy_window.mainloop()


def Renewable_resources():
    renewable_window = Toplevel()
    renewable_window.title("Foretree")
    renewable_window.config(padx=40, pady=40, bg=BLACK)
    heading = Label(renewable_window, text="Renewable Resources", bg=BLACK, font=("serif", 20, "bold"),fg="white")
    heading.grid(row=0, column=0, columnspan=4)
    background = PhotoImage(file="foretree.png")
    canvas = Canvas(renewable_window, width=322, height=326, highlightthickness=0)
    canvas.create_image(161, 163, image=background)
    canvas.grid(column=1, row=1, columnspan=2, padx=20, pady=20)
    wind_pic = Image.open("wind.jpg")
    wind_resized = wind_pic.resize((80, 30), Image.ANTIALIAS)
    wind_main = ImageTk.PhotoImage(wind_resized)
    wind_button = Button(renewable_window, command=wind_power, image=wind_main, highlightthickness=0,relief=FLAT)
    wind_button.grid(row=2, column=0)
    biomass_pic = Image.open("biomass.png")
    biomass_resized = biomass_pic.resize((80, 30), Image.ANTIALIAS)
    biomass_main = ImageTk.PhotoImage(biomass_resized)
    biomass_button = Button(renewable_window, command=biomass, image=biomass_main, highlightthickness=0,relief=FLAT)
    biomass_button.grid(row=3, column=1)
    solar_pic = Image.open("solar.png")
    solar_resized = solar_pic.resize((80, 30), Image.ANTIALIAS)
    solar_main = ImageTk.PhotoImage(solar_resized)
    solar_button = Button(renewable_window, image=solar_main, command=solar_energy, highlightthickness=0,relief=FLAT)
    solar_button.grid(row=3, column=2)
    waste_to_energy_pic = Image.open("waste.jpeg")
    waste_to_energy_resized = waste_to_energy_pic.resize((80, 30), Image.ANTIALIAS)
    waste_to_energy_main = ImageTk.PhotoImage(waste_to_energy_resized)
    waste_energy_button = Button(renewable_window, image=waste_to_energy_main, command=waste_to_energy, highlightthickness=0,relief=FLAT)
    waste_energy_button.grid(row=2, column=3)
    wind_label = Label(renewable_window, text="Wind Energy", bg=BLACK,fg="white")
    wind_label.grid(row=3, column=0)
    biomass_label = Label(renewable_window, text="Biomass", bg=BLACK, fg="white")
    biomass_label.grid(row=4, column=1)
    solar_label = Label(renewable_window, text="Solar Energy", bg=BLACK, fg="white")
    solar_label.grid(row=4, column=2)
    waste_to_energy_label = Label(renewable_window, text="Waste -> Energy", bg=BLACK, fg="white")
    waste_to_energy_label.grid(row=3, column=3)
    renewable_window.mainloop()


main_window = Tk()
main_window.title("Foretree")
main_window.config(width=1000, height=600, bg="white")
main_canvas = Canvas(width=1000, height=600, highlightthickness=0, bg=JET)
image = PhotoImage(file="main.png")
main_canvas.create_image(500, 300, image=image)
main_canvas.grid(row=1, column=1)

energy_capacity = Button(text="Energy Capacity", command=Energy_capacity, borderwidth=2, bg=PEACH,
                         highlightthickness=0, relief=FLAT)
main_canvas.create_window(60, 300, anchor=NW, window=energy_capacity)

renewable_resources = Button(relief=FLAT, text="Renewable Resources", command=Renewable_resources, borderwidth=2,
                             highlightthickness=0, bg=PEACH)
main_canvas.create_window(780, 300, anchor=NW, window=renewable_resources)
main_window.mainloop()
