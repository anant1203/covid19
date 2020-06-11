
import numpy as np
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nxtadmin_nxt_anant",
  passwd="rootpasswordgiven",
  database="nxtadmin_covid_us"
)
mycursor = mydb.cursor()	

us = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us.csv'
us_states='https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv'
us_county='https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv'

df_us = pd.read_csv(us, parse_dates=[0])
df_us_states = pd.read_csv(us_states, parse_dates=[0])
df_us_county = pd.read_csv(us_county, parse_dates=[0])


df_us['date']=df_us['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
df_us_states['date']=df_us_states['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
df_us_county['date']=df_us_county['date'].apply(lambda x: x.strftime('%Y-%m-%d'))



df_us=df_us.fillna(0)
sql = "INSERT INTO covid_live_us (date, cases, deaths,confirmed_cases, confirmed_deaths, probable_cases, probable_deaths) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = df_us.values.tolist()
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")



df_us_states=df_us_states.fillna(0)
sql = "INSERT INTO covid_live_us_states (date, state, fips, cases, deaths,confirmed_cases, confirmed_deaths, probable_cases, probable_deaths) VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s)"
val = df_us_states.values.tolist()
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")



df_us_county=df_us_county.fillna(0)
sql = "INSERT INTO covid_live_us_counties (date, county, state, fips, cases, deaths,confirmed_cases, confirmed_deaths, probable_cases, probable_deaths) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = df_us_county.values.tolist()
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")






