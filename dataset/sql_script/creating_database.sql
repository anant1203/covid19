-- creatation of the all tables 

use covid19;

show tables;

create table covid_us_states (
date DATE,
state VARCHAR(255),
fips INT,
cases INT,
deaths INT);

create table covid_us_counties (
date DATE,
county VARCHAR(255),
state VARCHAR(255),
fips INT,
cases INT,
deaths INT);

create table covid_live_us_states (
date DATE,
state VARCHAR(255),
fips INT,
cases INT,
deaths INT,
confirmed_cases INT,
confirmed_deaths INT,
probable_cases INT,
probable_deaths INT
);

create table covid_live_us_counties (
date DATE,
county VARCHAR(255),
state VARCHAR(255),
fips INT,
cases INT,
deaths INT,
confirmed_cases INT,
confirmed_deaths INT,
probable_cases INT,
probable_deaths INT);

create table covid_live_us (
date DATE,
cases INT,
deaths INT,
confirmed_cases INT,
confirmed_deaths INT,
probable_cases INT,
probable_deaths INT);

create table us_fips_code (
state varchar(255),
county_name varchar(255),
fips_state INT,
fips_county INT);

create table us_zip_code (
zip int,
zipcode_name varchar(255),
city varchar(255),
state varchar(255),
county_name varchar(255));

create table us_zip_code (
zip int,
zipcode_name varchar(255),
city varchar(255),
state varchar(255),
county_name varchar(255));

Create table new_facilites (
id varchar(255),
critical_care_capacity int,
critical_care_occupancy int,
critical_care_surge_capacity int,
intermediate_care_capacity int,
intermediate_care_occupancy int,
intermediate_care_surge_capacity int,
acute_care_capacity int, 
acute_care_occupancy int,
acute_care_surge_capacity int,
inpaitent_subtotal_capacity int,
inpaitent_subtotal_occupancy int,
inpaitent_subtotal_surge_capacity int,
observation_capacity int,
observation_occupancy int,
observation_surge_capacity int,
result_waiting_capacity int,
result_waiting_occupancy int,
result_waiting_surge_capacity int,
discharge_capacity int,
discharge_occupancy int,
discharge_surge_capacity int,
non_in_patient_subtotal int,
totals int);

Describe new_facilites;


insert into new_facilites
(id, critical_care_capacity, critical_care_occupancy, critical_care_surge_capacity, intermediate_care_capacity,
intermediate_care_occupancy, intermediate_care_surge_capacity, acute_care_capacity, acute_care_occupancy,
acute_care_surge_capacity, inpaitent_subtotal_capacity, inpaitent_subtotal_occupancy,
inpaitent_subtotal_surge_capacity, observation_capacity, observation_occupancy, observation_surge_capacity,
result_waiting_capacity, result_waiting_occupancy, result_waiting_surge_capacity, discharge_capacity,
discharge_occupancy, discharge_surge_capacity, non_in_patient_subtotal, totals) 
values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
