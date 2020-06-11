
-- Script to transfer data from csv to table
 
LOAD DATA LOCAL INFILE '/home/nxtadmin/covid_19/dataset/us-counties.csv'  
INTO TABLE covid_us_counties
FIELDS TERMINATED BY ','  
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS 
(@date,county,state,fips,cases,deaths) SET date  = STR_TO_DATE(@date,'%Y-%m-%d');

LOAD DATA LOCAL INFILE '/home/nxtadmin/covid_19/dataset/us-states.csv'  
INTO TABLE covid_us_states
FIELDS TERMINATED BY ','  
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS 
(@date,state,fips,cases,deaths) SET date  = STR_TO_DATE(@date,'%Y-%m-%d');

LOAD DATA LOCAL INFILE '/home/nxtadmin/covid_19/datase/us.csv' 
INTO TABLE covid_us
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@date,cases,deaths)
SET date  = STR_TO_DATE(@date,'%Y-%m-%d');


LOAD DATA LOCAL INFILE '/home/anant/Desktop/covid19-master/dataset/US_FIPS_Codes[1].csv' 
INTO TABLE us_fips_code
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 2 ROWS
(state,county_name,fips_state,fips_county);

LOAD DATA LOCAL INFILE '/home/anant/Desktop/covid19-master/dataset/usazipcode-1512j[1].csv' 
INTO TABLE us_zip_code
LINES TERMINATED BY '\n'
IGNORE 2 ROWS
(zip,zipcode_name,city,state,county_name);


