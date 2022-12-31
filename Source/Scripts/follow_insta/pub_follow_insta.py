import pandas as pd

arquivo= 'C:/Users/natha/Documents/Arquivos/Source/follow_insta/follow_insta.csv'

df = pd.read_csv(arquivo, encoding='unicode_escape')
df = df.drop(columns='Brand\naccount').drop(columns='Rank')
df = df.rename(columns={'Followers(millions)[2]':'Followers(millions)'})
html = df.to_html('teste_insta.html')