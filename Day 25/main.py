# with open("weather_data.csv") as data:
#     weather_data = data.readlines()
#     print(weather_data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1].isdigit():
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)

# temp_list = data["temp"].to_list()
# # average = round(sum(temp_list) / len(temp_list), 2)
# # print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# Get data in columns
# print(data[data["condition test"] == "Sunny"])
# print(data[data.day == "Monday"])
# print(data.condition-test)

# # Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# celsius_1 = monday.temp
# Fahrenheit_1 = (celsius_1 * 1.8) + 32
# print(Fahrenheit_1)

# data_dict = {
#     "student": ["Any", "James", "Yash"],
#     "scores": [76, 56, 65]
# }
# data_df = pandas.DataFrame(data_dict)
# data_df.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}
data_df = pandas.DataFrame(data_dict)
data_df.to_csv("squirrel_count.csv")
