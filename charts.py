# Donal Rynne - Data Analytics for Business - Final Project (Project Rubric) #Presentation

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# File import and treatment section, assign filename
file = 'output.csv'

# Import file: data
medals = pd.read_csv(file, sep=',', na_values=['Nothing'])


# File review and summary section
# Display sample data of the DataFrame
print("Olympic years in scope: " + str((medals['Year'].unique())))
print("")
print("All country participants in the period: " + str((medals['Country'].unique())))
print("")
#print(medals.columns)
#print(medals.isnull().sum())
#print(medals.head(5))

# Display max medals count by country
print("Max amount of gold medals by one country at any one Olympic games: " + str((medals["Gold"].max())))
print("Max amount of silver medals by one country at any one Olympic games: " + str((medals["Silver"].max())))
print("Max amount of bronze medals by one country at any one Olympic games: " + str((medals["Bronze"].max())))


yearly_view = (medals.pivot_table (index = "Country", columns="Year",values=['Gold'], fill_value=0))
print(yearly_view)

# Display Gold medal wins by reference to the relative wealth of countries
medals.groupby(["GDP_Level", "Gold"]).sum()
wealthiest_countries = (medals.pivot_table (index = "Country", columns="GDP_Level",values=['Gold'], fill_value="0"))
print(wealthiest_countries)

# Display Gold Medal wins by reference to the most populous countries
medals.groupby(["Pop_Level", "Gold"]).sum()
populous_countries = (medals.pivot_table (index = "Country", columns="Pop_Level",values=['Gold'], fill_value="0"))
print(populous_countries)

#Display countries with the most Gold medals
top_4_countries_by_year = medals.groupby('Country')['Gold'].sum().sort_values(ascending=False).head(4)
print(top_4_countries_by_year)





#Display Charts section
# List top performing countries by ref to gold medals
top_countries = ['USA', 'RUS', 'GBR', 'CHN', 'JPN'] # Note Japan only entered top 4 only when Olympics were in Japan 2020
team_medals = pd.pivot_table(medals,index = 'Year',columns = 'Country',values = 'Gold',aggfunc = 'sum')[top_countries]
team_medals.plot(linestyle = '-', marker = 's', linewidth = 3)
plt.xlabel('Olympic Year')
plt.ylabel('Number of Medals')
plt.title('Top Countries - Olympic Performance Comparison',fontsize=20)
plt.grid()
plt.show()

#Display medal wins against population level of the countries
plt.figure
sns.catplot(x='Pop_Level',kind='count',data=medals, order=medals.Pop_Level.value_counts().index)
plt.title('Gold Medal wins versus population level',fontsize=20)
plt.xlabel('Population Size',fontsize=14)
plt.ylabel('Medal Count',fontsize=14)
plt.grid()
plt.show()


medals.groupby('GDP_Level')[['Gold','Bronze','Silver']].sum().plot.bar(color=['gold','red','grey'])
plt.xlabel('Country Wealth',fontsize=12)
plt.ylabel('Medal Count',fontsize=12)
plt.title('All Countries All medals by GDP per capita',fontsize=20)
plt.xticks(rotation=0)
plt.grid()
plt.show()


# Focus on Ireland performance
# Display ALL Irish medal wins
medals[medals['Country']=='IRL'][['Gold','Bronze','Silver']].sum().plot.bar(color=['gold','red','grey'])
plt.xlabel('IRELAND OLYMPIC MEDALS TOTAL',fontsize=14)
plt.ylabel('TOTAL MEDALS',fontsize=14)
plt.title('Total Irish Olympic Medal Wins since 1970',fontsize=20)
plt.xticks(rotation=0)
plt.grid()
plt.show()

# Display ALL Irish medal wins
ireland_results = medals[medals['Country']=='IRL'].sort_values(['Year'], ascending=True)
print (ireland_results)
sns.barplot(y='Gold', x='Year' , data=ireland_results.sort_values(['Gold']),color="green")
plt.xlabel('Olympic Year',fontsize=14)
plt.ylabel('Medal Count',fontsize=14)
plt.title('All Irish Gold Medal Wins',fontsize=22)
plt.xticks(rotation=0)
plt.show()


# Focus on USA performance at 1984 games
USA_results = medals[medals['Country']=='USA'].sort_values(['Year'], ascending=True)
print (USA_results)
sns.barplot(y='Gold', x='Year' , data=USA_results.sort_values(['Gold']),color="blue")
plt.xlabel('USA performance by year',fontsize=10)
plt.ylabel('Year',fontsize=10)
plt.title('All USA Gold Medal Wins by year',fontsize=20)
plt.grid()
plt.show()

# Display ALL USA medal wins
medals[medals['Country']=='USA'][['Gold','Bronze','Silver']].sum().plot.bar(color=['gold','red','grey'])
plt.xlabel('USA OLYMPIC MEDALS TOTAL',fontsize=14)
plt.ylabel('TOTAL MEDALS',fontsize=14)
plt.title('Total USA Olympic Medal Wins since 1970',fontsize=20)
plt.xticks(rotation=0)
plt.grid()
plt.show()


# Focus on China performance since 1984
# Display ALL Chinese medal wins
china_results = medals[medals['Country']=='CHN'].sort_values(['Year'], ascending=True)
print (china_results)
sns.barplot(y='Gold', x='Year' , data=china_results.sort_values(['Gold']),color="red")
plt.xlabel('China performance by year',fontsize=20)
plt.ylabel('Year',fontsize=10)
plt.title('All Chinese Gold Medal Wins since 1984',fontsize=20)
plt.grid()
plt.show()

