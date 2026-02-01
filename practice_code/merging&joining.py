# pd.merge(df1, df2, on="Column_Name", how="type of join")
import pandas as pd

# customer dataframe
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Ramesh', 'Suresh', 'Kalpesh']
})

# order dataframe
df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 4],
    'OrderAmount': [250, 450, 350]
})
# merge
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="outer")
# print("inner join")
 #print("outer join")
# print("right join ")
# print("left join ")
print(df_merged)


### --- Merging & Joining --- ###

# vertically: (row-wise)
# horizontally: (column-wise)

# Concatenation Syntax:
# pd.concat([df1, df2], axis=0, ignore_index=True)

# [df1, df2]      -> List of DataFrames to combine
# axis = 1        -> horizontal (column wise)
# ignore_index    -> True (resets index to 0, 1, 2...)


# vertically
import pandas as pd

# region1
df_Region1 = pd.DataFrame({
    'CustomerID': [1, 2],
    'Name': ['Gopal', 'Raju']
})

# region2
df_Region2 = pd.DataFrame({
    'CustomerID': [3, 4],
    'Name': ['Shyam', 'Baburao']
})

# concatenate vertically
df_concat = pd.concat([df_Region1, df_Region2],axis=1,ignore_index=True)
print(df_concat)
