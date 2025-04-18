import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('video_game.csv')
print(df.head(20))
print(df.info())
print('Shape of Dataset:',df.shape)
print('columns:',df.columns.tolist())
print(df.describe())
print(df.isnull().sum())


df.dropna(inplace=True)
print(df.shape)

#Top 10 best selling game
top10 = df.sort_values(by='Global_Sales', ascending=False).head(5)
print('Top 10 best game selling')
print(top10[['Name', 'Platform', 'Global_Sales']])


# average genre-wise global_sales:
Genre_sale=df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(5)
print('Genre-wise Average Global Sales:')
print(Genre_sale)


#Year-wise total sale
year_sale = df.groupby('Year')['Global_Sales'].sum().sort_values(ascending=False)
print('Year-wise total sale and profit:')
print(year_sale)


#region-wise total sale 
global_sale=df.groupby('Region')[['Global_Sales','Global_Profit']].sum().sort_values(by='Global_Sales',ascending=False)
print('Global-wise sale:')
print(global_sale)


#platform-wise sale or profit
platform_total = df.groupby('Platform')[['Global_Sales', 'Global_Profit']].sum().sort_values(by='Global_Sales', ascending=False).head(7)
print(platform_total)



# Top 5 best selling game...
plt.figure(figsize=(12,8),facecolor='lightgray')
sns.set_style('darkgrid')
colors = ['lightseagreen', 'lightcoral', 'lightskyblue', 'palevioletred', 'lightgreen']
sns.barplot(x='Name', y='Global_Sales', data=top10,width=0.4,align='edge',palette=colors,linestyle='-',linewidth=3,edgecolor='black')
plt.title('Top 5 Best-Selling Video Games (Global)',fontsize=18,fontweight='semibold',fontname='arial',color='darkblue')
plt.xlabel('Game Tittle',fontsize=16,  color='darkblue', fontname='Arial',fontweight='bold')
plt.ylabel('Global_Sales',fontsize=17, color='darkblue', fontname='arial',fontweight='bold')
plt.xticks(fontsize=11, fontweight='bold', color='darkred')
plt.yticks(fontsize=13, fontweight='bold', color='darkred')
plt.grid(True, linestyle='-', alpha=0.4)
plt.show()


#year-wise total-sale
plt.figure(figsize=(10, 6),facecolor='lightgray')
sns.set_style("darkgrid")
year_sale.plot(kind='line',marker="o",markersize=5, color="red",linestyle='-')
plt.title('Global Video Game Sales Over the Years',fontsize=15,fontweight='semibold',fontname='arial',color='darkblue')
plt.fill_between(year_sale.index, year_sale, color='lightcoral', alpha=0.4)
plt.xlabel('Year',fontsize=15,fontweight='semibold',fontname='arial',color='darkblue')
plt.ylabel('Total Global Sales',fontsize=15,fontweight='semibold',fontname='arial',color='darkblue')
plt.xticks(fontsize=11, fontweight='bold', color='darkred')
plt.yticks(fontsize=11, fontweight='bold', color='darkred')
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()


#Region-wise sale
plt.figure(figsize=(10, 6), facecolor='lightgray')
sns.set_style("darkgrid")
plt.scatter(global_sale.index, global_sale['Global_Sales'], color='blue', label='Global Sales', alpha=0.7, edgecolor='black', marker='*', s=200)
plt.scatter(global_sale.index, global_sale['Global_Profit'], color='red', label='Global Profit', alpha=0.7, edgecolor='black', marker='*', s=200)
plt.title('Global Sales vs Global Profit by Region', fontsize=14, fontweight='semibold', fontname='Arial', color='darkblue')
plt.xlabel('Region', fontsize=15, fontweight='semibold', fontname='Arial', color='darkblue')
plt.ylabel('Value', fontsize=15, fontweight='semibold', fontname='Arial', color='darkblue')
plt.xticks(rotation=45, fontsize=12, fontweight='bold', color='black')
plt.yticks(fontsize=12, fontweight='bold', color='black')
plt.grid(True, linestyle="-", alpha=0.2)
plt.legend(title='Region', loc='upper right')
plt.tight_layout()
plt.show()



#Genre-wise sale
plt.figure(figsize=(6, 6), facecolor='lightgray')
colors = ['lightseagreen', 'lightcoral', 'lightskyblue', 'palevioletred', 'lightgreen']
explode=[0.1,0.1,0.1,0.1,0.1]
plt.pie(Genre_sale.values, labels=Genre_sale.index, autopct='%d%%', startangle=140, colors=colors,shadow=True,explode=explode, wedgeprops={'edgecolor': 'black', 'linewidth': 2, 'linestyle': '-'},textprops={'fontsize': 13, 'color': 'black', 'fontweight': 'bold'})
plt.title('Genre-wise Global Sales Distribution',fontsize=14, fontweight='semibold', fontname='Arial', color='darkblue')
plt.tight_layout()
plt.show()


#platform-wise total_sale and profit
plt.figure(figsize=(12, 8), facecolor='lightgray')
sns.set_style("darkgrid")
platforms = platform_total.index
sales = platform_total['Global_Sales']
profit = platform_total['Global_Profit']
plt.bar(platforms, sales, label='Global Sales', color='palevioletred', align='edge',linestyle='-',linewidth=3,edgecolor='black')
plt.bar(platforms, profit, bottom=sales, label='Global Profit', color='tomato', align='edge',linestyle='-',linewidth=3,edgecolor='black')
plt.title('Platform-wise Global Sales and Profit',fontsize=14, fontweight='semibold', fontname='Arial', color='darkblue')
plt.xlabel('Platform',fontsize=14, fontweight='semibold', fontname='Arial', color='darkblue')
plt.ylabel('Total Value', fontsize=14, fontweight='semibold', fontname='Arial', color='darkblue')
plt.xticks(fontsize=12, fontweight='bold', color='darkred')
plt.yticks(fontsize=12,fontweight='bold', color='darkred')
plt.legend(loc='upper right', title='Sale and Profit', fontsize=12)
plt.show()


