from tkinter.font import names

from numpy.ma.extras import column_stack

# 1.columns,rows?
# 2.what type of?
# 3.missing data?
# info()
# method
# -number of rows and column
# -column names
# -int64 float64 object
# -non null counts
# -memory usage of the data frame

import pandas as pd
df=pd.read_csv(r"C:\Users\Ratul\Downloads\sales_data_sample (1).csv",encoding="latin1")
print("Displaying the info of dataset")
#print(df.to_string())
print(df.info())
