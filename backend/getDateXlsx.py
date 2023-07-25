import pandas as pd 


df_czasy_wykonan = pd.read_excel('C:/Users/Tomasz/Desktop/czasy_wykonan.xlsx')

df_sort_czasy_wykonan = df_czasy_wykonan.sort_values('czas')

print(df_sort_czasy_wykonan)


