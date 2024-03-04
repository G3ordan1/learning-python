import pandas as pd 

df = pd.DataFrame({"col1": ["Sun", "Sun", "Moon", "Earth", "Moon", "Venus"]})

ids = [11, 22, 33, 44, 55, 66, 77]
countries = ['Seattle', 'London', 'Lahore', 'Berlin', 'Abuja']
 
df = pd.DataFrame(list(zip(ids, countries)),
                  columns=['Ids', 'Cities'])

df

y = pd.get_dummies(df.Cities, prefix='City')
print(y.head())
