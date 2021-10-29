#***--- 2.3.1 ---***

import pandas as pd
file_path = r'..\data\topic2\data'
file_name =  "stock_data.csv"
full_file_name = file_path + "\\" + file_name
df = pd.read_csv(full_file_name, skiprows=0) # , parse_dates=["Date Time"])
print(df)
df_new = df[::2]
print(df_new)
df_new.to_csv(r"..\data\topic2\data\new_stock.csv", index=False)


import pandas as pd
def convert_negative_to_zero(v):
    if isinstance(v, str): return v
    if v < 0:
        return 0
    else:
        return v

my_converts = { "eps": convert_negative_to_zero,
                "revenue": convert_negative_to_zero,
                "price": convert_negative_to_zero}

file_path = r'..\data\topic2\data'
file_name =  "stock_data.xlsx"
full_file_name = file_path + "\\" + file_name

df = pd.read_excel(full_file_name, sheet_name="Sheet1", converters=my_converts
     ) # , parse_dates=["Date Time"])

new_full_file_name =  file_path + "\\" + "new_" + file_name
df.to_excel(new_full_file_name,sheet_name="stock price", index = False)
with pd.ExcelWriter(new_full_file_name) as writer:
    df.to_excel(writer, sheet_name="df1")
    df.to_excel(writer, sheet_name="df2", startrow=2, startcol=2)