import pandas
from pandas.core.frame import DataFrame

squirrel_data = pandas.read_csv("Squirrel_Data.csv")

# series method
gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
red_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Red"])

# list method
color_list = squirrel_data["Primary Fur Color"].to_list()
num_gray = color_list.count("Gray")
num_black = color_list.count("Black")
num_red = color_list.count("Cinnamon")

# make dictionary, convert to dataframe, write csv
colors_dict = {"color": ["gray", "black", "red"],
                "count": [num_gray, num_black, num_red]}
print(colors_dict)
color_df = DataFrame(data=colors_dict)
print(color_df)

color_df.to_csv("Squirrel_Colors.csv")