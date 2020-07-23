# %%
import pandas as pd
import numpy as np
# from subprocess import call

# rc = call("./data_get.sh")

df = pd.read_csv("BL-Flickr-Images-Book.csv")
df.head()


# Seleccionando Columnas
df[['Identifier', 'Place of Publication']]
df.loc[:, ['Identifier', 'Place of Publication']]
df.iloc[:, 0:3]
df.loc[lambda df: df['Identifier'] > 4000, :]
df[df['Identifier'] > 4000]
df.loc[df['Identifier'] > 4000, ['Identifier', 'Place of Publication']]

df.columns.str.startswith('C')
pd.Series(df.columns)
df[df.columns[pd.Series(df.columns).str.startswith('C')]]
df[df.columns[pd.Series(df.columns.str.startswith('C'))]]


df = pd.read_csv("BL-Flickr-Images-Book.csv")

# Eliminando Columnas

to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']

df.drop(to_drop, inplace=True, axis=1)
# df.drop(columns=to_drop, inplace=True) # Version más legible
df.head()
# %%

# Fijando Index

df['Identifier'].is_unique
df = df.set_index('Identifier')
# df.set_index('Identifier', inplace=True) # Para evitar asignacion por = se puede usar inplace

df.head()

# %%
# Buscando registros
# Primero loc busca por index
df.loc[206]

# Segundo iloc busca por posición
df.iloc[0]
# %%
# Dando orden a los datos
type(df)
df.info()

df['Place of Publication'].value_counts()

df.loc[1905:, 'Date of Publication'].head(10)

# Ajustando fechas de publicación con regular expressions
# A particular book can have only one date of publication. Therefore, we need to do the following:

# Remove the extra dates in square brackets, wherever present: 1879 [1878]
# Convert date ranges to their “start date”, wherever present: 1860-63; 1839, 38-54
# Completely remove the dates we are not certain about and replace them with NumPy’s NaN: [1897?]
# Convert the string nan to NumPy’s NaN value
# Synthesizing these patterns, we can actually take advantage of a single regular expression to extract the publication year:

regex = r'^(\d{4})'
extr = df['Date of Publication'].str.extract(regex, expand=False)
extr
df['Date of Publication'] = pd.to_numeric(extr)
df['Date of Publication'].dtype
df.loc[1905:, 'Date of Publication'].head(10)

df['Date of Publication'].isnull().sum() / len(df)
df['Date of Publication'].value_counts()

# %%
# Numpy y .str para limpiar datos
# NumPy’s np.where function, which is basically a vectorized form of Excel’s IF() macro.
df['Place of Publication'].head(10)
df.loc[4157862]
df.loc[4159587]

pub = df['Place of Publication']
london = pub.str.contains('London')
type(london)
london[:5]
oxford = pub.str.contains('Oxford')

# Nested where
df['Place of Publication'] = np.where(london, 'London',
                                      np.where(oxford, 'Oxford',
                                               pub.str.replace('-', ' ')))

df['Place of Publication'].head()

df['Place of Publication'].unique()
ciudad = df['Place of Publication'].value_counts()
type(ciudad)
len(df['Place of Publication'].unique())

# %%

# applymap Function
university_towns = []
with open('university_towns.txt') as file:
    for line in file:
        if '[edit]' in line:
            # Remember this `state` until the next is found
            state = line
        else:
            # Otherwise, we have a city; keep `state` as last-seen
            university_towns.append((state, line))

university_towns[:5]

towns_df = pd.DataFrame(university_towns,
                        columns=['State', 'RegionName'])

towns_df.head()

def get_citystate(item):
    if ' (' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item


towns_df1 =  pd.DataFrame(towns_df['State']).applymap(get_citystate)
towns_df2 =  towns_df['RegionName'].applymap(get_citystate)
towns_df =  towns_df.applymap(get_citystate)
# %%

# Renaming Columns and Skipping Rows

olympics_df = pd.read_csv('olympics.csv')
olympics_df.head()

olympics_df = pd.read_csv('olympics.csv', header=1)
olympics_df.head()

new_names =  {'Unnamed: 0': 'Country',
              '? Summer': 'Summer Olympics',
              '01 !': 'Gold',
              '02 !': 'Silver',
              '03 !': 'Bronze',
              '? Winter': 'Winter Olympics',
              '01 !.1': 'Gold.1',
              '02 !.1': 'Silver.1',
              '03 !.1': 'Bronze.1',
              '? Games': '# Games',
              '01 !.2': 'Gold.2',
              '02 !.2': 'Silver.2',
              '03 !.2': 'Bronze.2'}

olympics_df.rename(columns=new_names, inplace=True)