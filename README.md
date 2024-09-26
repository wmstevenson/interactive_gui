# Preface

This was not an exercise in exploratory analysis nor complex statistical methods. The desired outcomes of this project where to gain experience with imbeded functionalities from multiple libraries as well as get some experience with geometry managers and widget configuration. The entire project was completed in an a few hours and was intended to simulate a take home assignment which are becoming more popular for technical hiring procecees. 


# Interactive GUI for CO2 Emissions Data

This Python script provides an interactive graphical user interface (GUI) for visualizing CO2 emissions data. The data is sourced from an internet scavenged CSV file named `emissions_data.csv`.

## Features

The script provides the following features:

1. **Data Filtering**: The script filters the data to focus on Denmark, Sweden, Norway, and the average for EU countries.

2. **Data Visualization**: The script generates two types of plots:
    - Absolute CO2 emissions over time.
    - CO2 emissions per capita over time.

3. **Interactive GUI**: The script uses Tkinter and ttkbootstrap to create an interactive GUI. The GUI includes a slider to select the year, and buttons to switch between the two types of plots.

## Dependencies

The script requires the following Python libraries:
- pandas
- matplotlib
- tkinter
- ttkbootstrap

## Usage

To run the script, navigate to the directory containing `interactive_gui.py` and `emissions_data.csv`, and run the following command:

```bash
python interactive_gui.py
```

This will open the GUI, where you can interact with the data.

## Data Source

The data is expected to be in a CSV file named emissions_data.csv in the same directory as the script. I make no comment to the correctness of this data, it was merely pulled from elsewhere on the internet an could be easily be partially or entirely atrificially generated.



