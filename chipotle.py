import pandas as pd

df = pd.read_table('orders.tsv')
df.head()

items  = df.item_name.value_counts().plot(kind='bar')
items  = df.item_name.value_counts()[:10].plot(kind='bar')

df['item_price'] = df['item_price'].str.replace('$','')
df['item_price'] = df['item_price'].astype(float)

orders = df.groupby('order_id').sum()
orders.head()
orders['item_price'].describe()

descriptions = df.groupby(["item_name", "choice_description"])["order_id"].count().reset_index(name="count")

descriptions = descriptions[descriptions['item_name'].str.contains("Chicken Bowl")]
descriptions.sort(['count'], ascending=False)[:10]

descriptions = descriptions[descriptions['item_name'].str.contains("Canned Soda")]
descriptions.sort(['count'], ascending=False)
