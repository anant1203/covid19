from __future__ import print_function
import pandas as pd
from datetime import date, datetime, timedelta
import mysql.connector
import flask
from flask import request, render_template

### Database Connection:
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rootpasswordgiven",
  database="covid19"
)
mycursor = mydb.cursor(buffered=True)
mycursor1 = mydb.cursor(buffered=True)

## defining application
app = flask.Flask(__name__,template_folder='/home/anant/Desktop/covid19-master/template')
app.config["DEBUG"] = True

### defining home of the application
@app.route('/')
def home():
    return render_template('index.html')


### State Details:
@app.route('/api/covid/state_all', methods=['GET'])
def state_all():
    query1=("Select state, count(fips), count(cases), count(deaths) from covid_us_states group by state;")
    mycursor.execute(query1)
    df1 = pd.DataFrame(columns=['state','fips','cases', 'deaths'])
    for state, fips, cases, deaths in mycursor:
        df1 = df1.append({"state":state,"fips":fips,"cases":cases,"deaths": deaths},ignore_index=True)

    query2=("Select state, count(fips), count(cases), count(deaths) from covid_live_us_states group by state;")
    df2 = pd.DataFrame(columns=['state','fips','cases', 'deaths'])
    mycursor.execute(query2)
    for state, fips, cases, deaths in mycursor:
         df2=df2.append({"state":state,"fips":fips,"cases":cases,"deaths": deaths},ignore_index=True)

    df1 = df1.set_index('state')
    df2 = df2.set_index('state')
    df1 = df1.add(df2)
    
    return df1.to_json(orient='table')
    

### County details:
@app.route('/api/covid/county_all', methods=['GET'])
def county_all():
    query3=("Select county, count(fips), count(cases),count( deaths) from covid_us_counties group by county;")
    mycursor.execute(query3)
    df3 = pd.DataFrame(columns=['county','fips','cases', 'deaths'])
    for county, fips, cases, deaths in mycursor:
        df3 = df3.append({"county":county,"fips":fips,"cases":cases,"deaths": deaths},ignore_index=True)

    query4=("Select county, count(fips), count(cases),count( deaths) from covid_live_us_counties group by county;")
    mycursor.execute(query4)
    df4 = pd.DataFrame(columns=['county','fips','cases', 'deaths'])
    for county, fips, cases, deaths in mycursor:
        df4 = df4.append({"county":county,"fips":fips,"cases":cases,"deaths": deaths},ignore_index=True)

    df3=df3.set_index('county')
    df4=df4.set_index('county')
    df3=df3.add(df4)
    df3.head()
    return(df3.to_json(orient='table'))


### US Details:
@app.route('/api/covid/us_all', methods=['GET'])
def us_all():
    query5=("Select cases, deaths from covid_us;")
    mycursor.execute(query5)
    df5 = pd.DataFrame(columns=['cases', 'deaths'])
    for cases, deaths in mycursor:
        df5 = df5.append({"cases":cases,"deaths": deaths},ignore_index=True)

    query6=("Select cases , deaths from covid_live_us;")
    mycursor.execute(query6)
    df6 = pd.DataFrame(columns=['cases', 'deaths'])
    for cases, deaths in mycursor:
        df6 = df6.append({"cases":cases,"deaths": deaths},ignore_index=True)

    df5=df5.append(df6,ignore_index=True)
    df5.head()
    return(df5.to_json(orient='table'))


#States wise county details:
@app.route('/api/covid/states_wise_county/', methods=['GET','POST'])
def state_wise_county():
    state_name =  request.get_json()['state_name']
    query3=("Select county, count(fips), count(cases),count( deaths) from covid_us_counties where state= \'{}\' group by county;")
    mycursor.execute(query3.format(state_name))
    df3 = pd.DataFrame(columns=['county','fips','cases', 'deaths'])
    for county, fips, cases, deaths in mycursor:
        df3 = df3.append({"county":county,"fips":fips,"cases":cases,"deaths": deaths},ignore_index=True)

    query4=("Select county, count(fips), count(cases),count( deaths) from covid_live_us_counties where state= \'{}\' group by county;")
    mycursor.execute(query4.format(state_name))
    df4 = pd.DataFrame(columns=['county','fips','cases', 'deaths'])
    for county, fips, cases, deaths in mycursor:
        df4 = df4.append({"county":county,"fips":fips,"cases":cases,"deaths": deaths},ignore_index=True)
        
    df3=df3.set_index('county')
    df4=df4.set_index('county')
    df3=df3.add(df4)
    df3.head()
    
    return df3.to_json(orient='table')


#Confirmed and Probable: Cases / Deaths
@app.route('/api/covid/county_confirmed_proable/', methods=['GET','POST'])
def county_confirmed_proable():
    state_name = request.get_json()['state_name']
    query5=("Select county, count(confirmed_cases), count(probable_cases),count( confirmed_deaths) ,count( probable_deaths) from covid_live_us_counties where state= \'{}\' group by county;")
    mycursor.execute(query5.format(state_name))
    df5 = pd.DataFrame(columns=['county','confirmed_cases','probable_cases', 'confirmed_deaths', 'probable_deaths'])
    for county, confirmed_cases, probable_cases, confirmed_deaths, probable_deaths in mycursor:
        df5 = df5.append({"county":county,"confirmed_cases":confirmed_cases,"probable_cases":probable_cases,"confirmed_deaths": confirmed_deaths,"probable_deaths":probable_deaths},ignore_index=True)
   
    df5 = df5.set_index('county')
    return df5.to_json(orient='table')



#Lookup on city and state facilities
@app.route('/api/covid/lookup/', methods=['GET','POST'])
def lookup():
    
    city_name = request.get_json()['city']
    stat_id = request.get_json()['stat_id']
    
    query4=("SELECT * FROM covid19.Hospital_List where city=\'{}\' and stat_id = \'{}\';")
    mycursor.execute(query4.format(city_name, stat_id))
    
    df4 = pd.DataFrame(columns=mycursor.column_names)
    for id, name, address_1, city, stat_id,zipcode,FIPS,CBSA2015,CBSA2017,CBSA2018,RUCA,FORHP,SPECIALPAYMENT,phone,POS,capacity,BEDS,acute_occupancy in mycursor:
        df4 = df4.append({"id":id,"name":name,"address_1":address_1,"city":city,"stat_id":stat_id,"zipcode":zipcode,"FIPS":FIPS,
                    "CBSA 2015":CBSA2015,"CBSA 2017":CBSA2017,"CBSA 2018":CBSA2018,"RUCA Code":RUCA,
                     'FORHP Rural/Urban 2018':FORHP,
                     'SPECIAL PAYMENT':SPECIALPAYMENT,
                     'phone':phone,
                     'CERTIFIED BEDS, POS':POS,
                     'capacity':capacity,
                     'BEDS, PSF':BEDS,
                     'acute_occupancy':acute_occupancy},ignore_index=True)
        
    return df4.to_json(orient='table')


#inserting new facilities in a city/state
@app.route('/api/covid/new_facilites/', methods=['GET','POST'])
def new_facilites():
    
    id = request.get_json()['id']

    critical_care_capacity = request.get_json()['critical_care_capacity']
    critical_care_occupancy = request.get_json()['critical_care_occupancy']
    critical_care_surge_capacity = request.get_json()['critical_care_surge_capacity']

    intermediate_care_capacity = request.get_json()['intermediate_care_capacity']
    intermediate_care_occupancy = request.get_json()['intermediate_care_occupancy']
    intermediate_care_surge_capacity = request.get_json()['intermediate_care_surge_capacity']

    acute_care_capacity = request.get_json()['acute_care_capacity']
    acute_care_occupancy = request.get_json()['acute_care_occupancy']
    acute_care_surge_capacity = request.get_json()['acute_care_surge_capacity']

    inpaitent_subtotal_capacity = request.get_json()['inpaitent_subtotal_capacity']
    inpaitent_subtotal_occupancy = request.get_json()['inpaitent_subtotal_occupancy']
    inpaitent_subtotal_surge_capacity = request.get_json()['inpaitent_subtotal_surge_capacity']

    observation_capacity = request.get_json()['observation_capacity']
    observation_occupancy = request.get_json()['observation_occupancy']
    observation_surge_capacity = request.get_json()['observation_surge_capacity']

    result_waiting_capacity = request.get_json()['result_waiting_capacity']
    result_waiting_occupancy = request.get_json()['result_waiting_occupancy']
    result_waiting_surge_capacity = request.get_json()['result_waiting_surge_capacity']

    discharge_capacity = request.get_json()['discharge_capacity']
    discharge_occupancy = request.get_json()['discharge_occupancy']
    discharge_surge_capacity = request.get_json()['discharge_surge_capacity']

    non_in_patient_subtotal = request.get_json()['non_in_patient_subtotal']
    totals = request.get_json()['totals']
    
    print(id,critical_care_capacity,critical_care_occupancy,critical_care_surge_capacity,intermediate_care_capacity,
         intermediate_care_occupancy,intermediate_care_surge_capacity,acute_care_capacity,acute_care_occupancy,
         acute_care_surge_capacity,inpaitent_subtotal_capacity,inpaitent_subtotal_occupancy,
         inpaitent_subtotal_surge_capacity,observation_capacity,observation_occupancy,observation_surge_capacity,
         result_waiting_capacity,result_waiting_occupancy,result_waiting_surge_capacity,discharge_capacity,
         discharge_occupancy,discharge_surge_capacity,non_in_patient_subtotal,totals)
    
    val = [id,critical_care_capacity,critical_care_occupancy, critical_care_surge_capacity, intermediate_care_capacity,intermediate_care_occupancy,intermediate_care_surge_capacity,
          acute_care_capacity,acute_care_occupancy,acute_care_surge_capacity, inpaitent_subtotal_capacity,
          inpaitent_subtotal_occupancy,inpaitent_subtotal_surge_capacity, observation_capacity, observation_occupancy,
          observation_surge_capacity, result_waiting_capacity, result_waiting_occupancy, result_waiting_surge_capacity,
          discharge_capacity, discharge_occupancy, discharge_surge_capacity, non_in_patient_subtotal, totals]
    
    print(val)
    

    sql= "Insert into covid19.new_facilites (id, critical_care_capacity, critical_care_occupancy, critical_care_surge_capacity, intermediate_care_capacity,intermediate_care_occupancy, intermediate_care_surge_capacity, acute_care_capacity, acute_care_occupancy, acute_care_surge_capacity, inpaitent_subtotal_capacity, inpaitent_subtotal_occupancy,inpaitent_subtotal_surge_capacity, observation_capacity, observation_occupancy, observation_surge_capacity, result_waiting_capacity, result_waiting_occupancy, result_waiting_surge_capacity, discharge_capacity, discharge_occupancy, discharge_surge_capacity, non_in_patient_subtotal, totals) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    
    val = [id,critical_care_capacity,critical_care_occupancy, critical_care_surge_capacity, intermediate_care_capacity, intermediate_care_occupancy, intermediate_care_surge_capacity, acute_care_capacity, acute_care_occupancy,acute_care_surge_capacity, inpaitent_subtotal_capacity,
          inpaitent_subtotal_occupancy,inpaitent_subtotal_surge_capacity, observation_capacity, observation_occupancy,
          observation_surge_capacity, result_waiting_capacity, result_waiting_occupancy, result_waiting_surge_capacity,
          discharge_capacity, discharge_occupancy, discharge_surge_capacity, non_in_patient_subtotal, totals]
    
    mycursor.execute(sql, val)
    
    mydb.commit()
    
    
    return ("inserted")


    
app.run()
