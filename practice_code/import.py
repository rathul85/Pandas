import pandas as pd
#read data from csv file into dataframe
df=pd.read_csv(r"C:\Users\Ratul\Downloads\DimCustomers.csv",encoding="latin1")
#UTF-8
#df=pd.read_excel(r"SampleSuperstore.xlsx")
#df=pd.read_json("sample_Data.json")
#print(df)
#gcsfs library-goggle cloud
print(df.to_string(index=False))



# print(df),Truncated: Large datasets are shortened with ... in the middle.,Quick preview of the data structure.
# print(df.to_string()),Expanded: Shows every single row and column without hiding anything.,Full data check to see every detail.
# print(df.to_string(index=False)),"Expanded + No Serial No.: Shows all data but removes the left-side index numbers (0, 1, 2...).",Clean text format for reports or final output.
