use covid19;

show tables;

describe covid_us;

Select count(*) 
from covid19.covid_us;

Select count(*) 
from covid19.covid_us_counties;

Select count(*) 
from covid19.covid_us_states;

Select count(*) 
From covid_live_us;

Select *
From covid_live_us_counties;

Select county, count(fips), count(cases),count( deaths) 
from covid_us_counties  
group by county;

Select county, count(confirmed_cases), count(probable_cases),count( confirmed_deaths) ,count( probable_deaths) 
from covid_live_us_counties  
where state='georgia'
group by county;

describe covid_live_us_counties;

select *
from us_fips_code;

select *
from us_zip_code;







