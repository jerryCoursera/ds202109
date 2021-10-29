#***--- 2.2.1 ---***
# import numpy as np
# import pandas as pd
# df = pd.read_csv(r'..\data\topic2\data\stock_data.csv')
# df.head(5)
# df.tail(5)
#
# #***--- 2.2.2 ---***
# import pandas as pd
# df = pd.read_csv(r'..\data\topic2\data\msft.csv', skiprows=1, nrows=4) # , parse_dates=["Date Time"])
# print(df.columns)
# print(df.shape)
# df.set_index("Date Time", inplace=True)
# print(df)
# print(df.loc[["8/17/2017 9:00:00 AM","8/17/2017 9:15:00 AM","8/17/2017 9:30:00 AM","8/17/2017 9:45:00 AM"]])
# df = pd.read_csv(r'..\data\topic2\data\msft.csv', skiprows=1, parse_dates=["Date Time"])

#print(df["8/17/2017 10:00:00": "8/17/2017 11:00:00"])

#***--- 2.2.3 ---***
import pandas as pd
my_dict = {"Date Time": [
"8/17/2017 9:00:00 AM",
"8/17/2017 9:15:00 AM",
"8/17/2017 9:30:00 AM",
"8/17/2017 10:00:00 AM",
"8/17/2017 10:30:00 AM",
"8/17/2017 11:00:00 AM"
    ],
"Price": [
72.38, 71, 71.67, 72.8, 73, 72.5]
}
df_dict = pd.DataFrame(my_dict)
print(df_dict)

my_tuple = [ ("8/17/2017 9:00:00 AM",  72.38),
                ("8/17/2017 9:15:00 AM",  71),
( "8/17/2017 9:30:00 AM",  71.67),
("8/17/2017 10:00:00 AM",  72.8),
("8/17/2017 10:30:00 AM",  73),
( "8/17/2017 11:00:00 AM", 72.5)
            ]
df_tuple = pd.DataFrame(my_tuple, columns = ["Date Time", "Price"])
print(df_tuple)


my_list = [
{ "Date Time": "8/17/2017 9:00:00 AM", "Price": 72.38},
{ "Date Time": "8/17/2017 9:15:00 AM", "Price": 71},
{ "Date Time": "8/17/2017 9:30:00 AM", "Price": 71.67},
{ "Date Time": "8/17/2017 10:00:00 AM", "Price": 72.8},
{ "Date Time": "8/17/2017 10:30:00 AM", "Price": 73},
{ "Date Time": "8/17/2017 11:00:00 AM", "Price": 72.5}
            ]
import datetime
df_list = pd.DataFrame(my_list)
print(df_list)

price_list =my_dict["Price"]
dt_list = my_dict["Date Time"]
date_list = [x.split(" ")[0] for x in dt_list]
time_list = [datetime.datetime.strptime(x, "%m/%d/%Y %I:%M:%S %p").time().strftime("%H:%M:%S") for x in dt_list]
my_dict_new = {"riqi":date_list, "shijian": time_list, "jiage": price_list}
print(my_dict_new)

