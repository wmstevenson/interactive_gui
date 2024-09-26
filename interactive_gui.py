import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import ttkbootstrap as ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.style.use("seaborn-v0_8-pastel")

df = pd.read_csv("emissions_data.csv")
df = df.fillna(0)


# subset of original df containing Danish data only
den_df = df[df["country"] == "Denmark"]
# subset of original df containing Swedish data only
swe_df = df[df["country"] == "Sweden"]
# subset of original df containing Norwegian data only
nor_df = df[df["country"] == "Norway"]


"""
Here I calculate absolute emissions figures for the Denmark, Sweden and Norwary as well as the EU average.
"""

# List of EU countries
eu_countries = [
    "Austria",
    "Belgium",
    "Bulgaria",
    "Croatia",
    "Republic of Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Ireland",
    "Italy",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Netherlands",
    "Poland",
    "Portugal",
    "Romania",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
]

# Filter the dataframe to only include European countries
eu_df = df[df["country"].isin(eu_countries)]

# Group by 'year' and calculate the sum of 'co2'
total_eu_emissions_per_year = eu_df.groupby("year")["co2"].sum()

# Calculate the number of EU countries
num_eu_countries = len(eu_countries)

# Calculate the average emissions of countries in the EU
eu_countries_avg_emissions_per_year = total_eu_emissions_per_year / num_eu_countries


"""
Here I calculate the relative emissions figures for the Denmark, Sweden and Norwary as well as the EU average.
"""

# Sum of population for each year
eu_population_per_year = eu_df.groupby("year")["population"].sum()

# Calculate the average emissions per capita for countries in the EU
avg_emissions_per_year = total_eu_emissions_per_year / eu_population_per_year

"""
Here I create the functions that the GUI widgets trigger.
"""


def check0():
    check_var0.set(True)
    check_var1.set(False)
    plot()


def check1():
    check_var0.set(False)
    check_var1.set(True)
    plot()


def plot():
    if check_var0.get():
        plot_0()
    elif check_var1.get():
        plot_1()
    else:
        pass


def plot_0():
    ax0.clear()
    plt.title("Absolute CO2 emissions")
    plt.plot(den_df["year"], den_df["co2"], label="Denmark")
    plt.plot(swe_df["year"], swe_df["co2"], label="Sweden")
    plt.plot(nor_df["year"], nor_df["co2"], label="Norway")
    plt.plot(
        eu_countries_avg_emissions_per_year.index,
        eu_countries_avg_emissions_per_year,
        label="EU",
    )
    plt.axvline(x=label_var.get(), c="black", label=f"Year: {label_var.get()}")
    plt.legend()
    canvas0.draw()


def plot_1():
    ax0.clear()
    plt.title("CO2 emissions per capita")
    plt.plot(den_df["year"], den_df["co2"] / den_df["population"], label="Denmark")
    plt.plot(swe_df["year"], swe_df["co2"] / swe_df["population"], label="Sweden")
    plt.plot(nor_df["year"], nor_df["co2"] / nor_df["population"], label="Norway")
    plt.plot(avg_emissions_per_year.index, avg_emissions_per_year, label="EU")
    plt.axvline(x=label_var.get(), c="black", label=f"Year: {label_var.get()}")
    plt.legend()
    canvas0.draw()


"""
Here I create an interactive board using Tkinter.
"""


window = ttk.Window(themename="cerculean")
window.title("Interactive board")
window.geometry("900x600")


side_frame = ttk.Frame(window)

max_year = eu_df["year"].max()
min_year = eu_df["year"].min()


def year_num(value):
    year = slider_var.get()
    label_var.set(year)
    plot()


slider_var = ttk.IntVar(value=min_year)
slider = ttk.Scale(
    side_frame,
    command=year_num,
    from_=max_year,
    to=min_year,
    value=1,
    orient="vertical",
    length=300,
    variable=slider_var,
)
slider.pack(padx=40, pady=5)

label_var = ttk.IntVar(value=min_year)
label = ttk.Label(side_frame, textvariable=label_var, font=("Courier", 32))
label.pack(padx=40, pady=5)


side_frame.pack(side=tk.LEFT)


charts_frame = ttk.Frame(window)


fig0, ax0 = plt.subplots()

figure_0_frame = ttk.Frame(window)

canvas0 = FigureCanvasTkAgg(fig0, master=figure_0_frame)
ax0.get_xaxis().set_visible(True)
ax0.get_yaxis().set_visible(True)
canvas0.get_tk_widget().pack()

button_frame = ttk.Frame(figure_0_frame)

check_var0 = tk.BooleanVar()
button0 = ttk.Button(button_frame, text="Absolute", command=check0)
button0.pack(side=tk.LEFT, padx=20)
check_var1 = tk.BooleanVar()
button1 = ttk.Button(button_frame, text="Relative", command=check1)
button1.pack(side=tk.RIGHT, padx=20)
button_frame.pack()

figure_0_frame.pack(side=tk.LEFT)


charts_frame.pack()
window.mainloop()