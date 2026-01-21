# understand the datset
# identify the problems
# plan next steps
#head () by default top 5 rows
#tail() by default bottom 5 rows
#head () 3 top 3 rows
#tail(n) 3 bottom 3 rows
import pandas as pd
df=pd.read_csv(r"C:\Users\Ratul\Downloads\sales_data_sample (1).csv",encoding="latin1")
print("Display Top 10 rows of first")
print(df.head(10))
print("Display bottom 10 rows of first")
print(df.tail(10))


