import pandas as pd
import numpy as np

df=pd.read_csv("covid.csv")
print(df.head())

print(df.isnull().sum)

print(df.shape)

print(df.duplicated().sum)

print(df.info())

print(df.columns)

print(df.describe())


df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
print(df)


#Every year covid case
Total_cases_by_year = df.groupby('year')['total_cases'].sum().reset_index()
print(Total_cases_by_year)

#Every year deaths 
Total_deaths_by_year=df.groupby('year')['total_deaths'].sum().reset_index()
print(Total_deaths_by_year)

#Every year vaccanation-wise trend
Total_vaccanation_by_year=df.groupby('year')['total_vaccinations'].sum().reset_index()
print(Total_vaccanation_by_year)

#continent-wise case
continent_wise_case=df.groupby('continent')['total_cases'].sum().reset_index()
print(continent_wise_case)

#continent-wise death
continent_wise_death=df.groupby('continent')['total_deaths'].sum().reset_index()
print(continent_wise_death)

#continent-wise vaccanation
continent_wise_vaccination=df.groupby('continent')['total_vaccinations'].sum().reset_index()
print(continent_wise_vaccination)

#death_rate by country
df['death_rate'] = (df['total_deaths'] / df['total_cases']) * 100
death_rate_by_country = df.groupby('location')['death_rate'].mean().reset_index()
print(death_rate_by_country)

#positive_rate by country
df['positive_rate']=(df['total_cases']/df['total_tests'])*100
positive_rate_by_country = df.groupby('location')['positive_rate'].mean().reset_index()
print(positive_rate_by_country)

#country and population-wwise total case
country_stats = df.groupby('location')[['population','total_cases']].sum().reset_index()
print(country_stats)

#country and population-wwise total positive
country_stats = df.groupby('location')[['population', 'positive_rate']].agg({'population': 'sum', 'positive_rate': 'mean'}).reset_index()
print(country_stats)



#top 5 country by covid_case
top_5_deaths = df.groupby('location')['total_cases'].sum().sort_values(ascending=False).head(5).reset_index()
print(top_5_deaths)

#Top 5 country by death
Top_5=df.groupby('location')['total_deaths'].sum().sort_values(ascending=False).head(5).reset_index()
print(Top_5)



# location-wise and sum total_vaccinations, people_vaccinated, and people_fully_vaccinated
vaccinated = df.groupby('location')[['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']].sum().reset_index()
print(vaccinated)


#cardivaoic death 
df['total_cardiovasc_deaths'] = (df['cardiovasc_death_rate'] * df['population']) / 100000
pd.options.display.float_format = '{:,.0f}'.format
location=df.groupby('location')[['population','total_cardiovasc_deaths']].sum().reset_index()
print(location)

#diabetes death
df['total_diabetes_prevalence'] = (df['diabetes_prevalence'] * df['population']) / 100000
location=df.groupby('location')[['population','total_diabetes_prevalence']].sum().reset_index()
print(location)


#top 5 gdp per capita country
total_gdp = df['gdp_per_capita'].sum()
country_gdp_percentage = df.groupby('location')['gdp_per_capita'].sum() / total_gdp * 100
top_5_countries = country_gdp_percentage.head(5).sort_values(ascending=False)
print(top_5_countries)

#top 5 extreme poverty country
total_poverty = df['extreme_poverty'].sum()
country_gdp_percentage = df.groupby('location')['extreme_poverty'].sum() / total_poverty * 100
top_5_countries = country_gdp_percentage.tail(5).sort_values(ascending=True)
print(top_5_countries)