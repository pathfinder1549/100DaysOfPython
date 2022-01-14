#import csv
import pandas

data = pandas.read_csv("weather_data.csv")
#print(data)

data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()

avg = data["temp"].mean()
max = data["temp"].max()
print(f"Average temp: {avg}, Max temp: {max}")

#get data in a row
print(data[data.temp == data.temp.max()])

#convert mondays temp
mon = data[data.day == "Monday"]
temp_F = float(mon.temp) *9/5 + 32
print(temp_F)
print(mon)
print(mon["day"])

#create dataframe
