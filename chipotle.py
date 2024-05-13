import pandas as pd

df = pd.read_table('orders.tsv')
print(df.head())

items  = df.item_name.value_counts().plot(kind='bar')
items.get_figure().savefig("fig1.png")
items  = df.item_name.value_counts()[:10].plot(kind='bar')

items.get_figure().savefig("fig2.png")
df['item_price'] = df['item_price'].str.replace('$','')
df['item_price'] = df['item_price'].astype(float)

orders = df.groupby('order_id').sum()
print(orders.head())
print(orders['item_price'].describe())

descriptions = df.groupby(["item_name", "choice_description"])["order_id"].count().reset_index(name="count")

desc = descriptions[descriptions['item_name'].str.contains("Chicken Bowl")]
desc.sort_values(['count'], ascending=False)[:10]

desc = descriptions[descriptions['item_name'].str.contains("Canned Soda")]
desc.sort_values(['count'], ascending=False)
