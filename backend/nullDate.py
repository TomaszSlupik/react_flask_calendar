import pandas as pd

null_xlsx = pd.read_excel('C:/Users/Bartosz/Desktop/null.xlsx')

no_value = null_xlsx.fillna('Brak')


print(no_value)
