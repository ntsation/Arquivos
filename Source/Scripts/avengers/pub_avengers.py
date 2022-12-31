import pandas as pd

arquivo= 'C:/Users/natha/Documents/Arquivos/Source/Scripts/avengers/avengers.csv'

df = pd.read_csv(arquivo, encoding='unicode_escape')
df = df.drop(columns = 'URL').drop(columns = 'Probationary Introl')
df = df[df.columns[0:7]]
df_ordenado = df.sort_values(by='Appearances',ascending=False)
html = df.to_html('avengers.html')